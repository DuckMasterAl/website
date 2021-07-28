import os, tinify
tinify.key = os.environ['api_key']
for x in eval(os.environ['added_files']):
  source = tinify.from_file(x)
  source.to_file(x)
