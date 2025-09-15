# chatbot-eval-demo

A demo repository for experimenting with chatbot evaluation using [Promptfoo](https://github.com/promptfoo/promptfoo). This repo provides a simple workflow to define prompts, generate evaluation templates, and run evaluations on your chatbot.

## Features

* Define custom prompts and evaluation rules
* Generate CSV templates compatible with Promptfoo
* Run evaluations via CLI or Red Team GUI

## Usage

1. **Set prompts and rules**
   Edit `prompt.py` to define your list of prompts and evaluation rules.

2. **Generate CSV template**
   Run `prompt.py` to generate a `.csv` file that will serve as a template for Promptfoo evaluation.

   ```bash
   python prompt.py
   ```

3. **Update YAML configuration**
   Update the generated YAML file with any additional settings required for Promptfoo evaluation.

4. **Run Promptfoo evaluation**
   You can run evaluations in two ways:

   * **CLI**: Run Promptfoo directly from the command line
   * **Red Team GUI**: Start the Red Team interface for interactive evaluation

     ```bash
     promptfoo redteam setup
     ```