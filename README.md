# Automatic Text Generation

This repository will continously make api calls to a [text-generation-ui](https://github.com/oobabooga/text-generation-webui) server and log the results to a file.  

## Usage
This assumes that you are running the text-generation-ui server and have the api turned on at port 5000.  
  
To use the repository, make a `config.json` file at the root of the project.  
File Defaults and explanation:
```
{
  "prefix": '', // Text to prepend to generation or input for every generation
  "num_generations": 100, // Number of times to generate output
  "save_interval": 5, // Number of generations to make before saving file
  "input_file": 'input.json', // file to read for input data, assumes it is a list of strings
  "output_file": 'generations.json', // file to write to for the generation data
  "use_input_file": True, // whether to use the input file or start with only prefix
  "num_tokens": 300, // number of tokens to generate
  "print_generations": False // whether to print the generations to the terminal
}
```
