import torch
from torch import nn
from transformers import LlamaForCausalLM, LlamaTokenizer

# Set the output directory
# output_dir = "./output_dir/"
output_dir = "./more_data10k"


tokenizer = LlamaTokenizer.from_pretrained(output_dir)
model = LlamaForCausalLM.from_pretrained(output_dir)

# Check if multiple GPUs are available and wrap the model with DataParallel
if torch.cuda.device_count() > 1:
    model = nn.DataParallel(model)

# Move the model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Generate text
def generate_text(prompt, max_length=1100, num_return_sequences=1, temperature=1, device='cuda' if torch.cuda.is_available() else 'cpu'):
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    

    # Access the underlying model if wrapped with DataParallel
    if isinstance(model, nn.DataParallel):
        model_to_use = model.module
    else:
        model_to_use = model


    output = model_to_use.generate(input_ids, max_length=max_length, temperature=temperature, num_return_sequences=num_return_sequences)
    return tokenizer.decode(output[0], skip_special_tokens=True)

if __name__ == "__main__":
    # Example usage
    while True:
        # Get user input
        prompt = input("Enter a prompt (type 'quit' to exit): ")

        if prompt.lower() == 'quit':
            break

        # Generate text based on user input
        generated_text = generate_text(prompt)
        print(generated_text)
