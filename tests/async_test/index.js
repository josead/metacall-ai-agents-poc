require("metacall");

const assistant = require("./assistant.py");
const { performance } = require("perf_hooks");

async function runAgent(prompt, idx) {
  const start = performance.now();
  console.log(`Task ${idx} started at ${new Date().toISOString()}`);
  const agent = await assistant.arun_agent(prompt);
  const end = performance.now();
  console.log(
    `Task ${idx} ended at ${new Date().toISOString()} (duration: ${(
      end - start
    ).toFixed(2)} ms)`
  );
  return agent;
}

async function runNodeAsync(prompt, idx) {
  const start = performance.now();
  console.log(`Task ${idx} started at ${new Date().toISOString()}`);
  const something = await new Promise((resolve) => {
    setTimeout(() => {
      resolve("something");
    }, Math.random() * 1000);
  });
  const end = performance.now();
  console.log(
    `Task ${idx} ended at ${new Date().toISOString()} (duration: ${(
      end - start
    ).toFixed(2)} ms)`
  );
  return something;
}

const prompts = [
  "What is the capital of France?",
  "Who wrote 'Pride and Prejudice'?",
  "What is the speed of light in m/s?",
];

async function main() {
  try {
    const totalStart = performance.now();
    const results = await Promise.all(
      prompts.map((prompt, idx) => runAgent(prompt, idx))
    );
    const totalEnd = performance.now();
    console.log("Results from Promise.all:", results);
    console.log(`Total elapsed time: ${(totalEnd - totalStart).toFixed(2)} ms`);
  } catch (err) {
    console.error("Error in Promise.all:", err);
  }
}

main();
