require("metacall");
var assistant = require("assistant.py");
var agent = assistant.run_agent("What is the capital of France?");
console.log(agent);

