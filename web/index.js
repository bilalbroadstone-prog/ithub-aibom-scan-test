const express = require("express");
const Anthropic = require("@anthropic-ai/sdk");
const { Configuration, OpenAIApi } = require("openai");
const { HfInference } = require("@huggingface/inference");

const app = express();
app.use(express.json());

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const openai = new OpenAIApi(new Configuration({ apiKey: process.env.OPENAI_API_KEY }));
const hf = new HfInference(process.env.HF_TOKEN);

app.post("/chat", async (req, res) => {
  const { prompt, provider } = req.body;
  if (provider === "anthropic") {
    const r = await anthropic.messages.create({
      model: "claude-3-5-sonnet-20240620", max_tokens: 512,
      messages: [{ role: "user", content: prompt }],
    });
    return res.json({ reply: r.content[0].text });
  }
  if (provider === "hf") {
    const r = await hf.textGeneration({ model: "mistralai/Mistral-7B-Instruct-v0.3", inputs: prompt });
    return res.json({ reply: r.generated_text });
  }
  const r = await openai.createChatCompletion({
    model: "gpt-4o", messages: [{ role: "user", content: prompt }],
  });
  res.json({ reply: r.data.choices[0].message.content });
});

app.listen(3000);
