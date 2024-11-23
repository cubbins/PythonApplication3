import subprocess

def list_conda_packages(env_name):
    try:
        # Use the absolute path to the conda executable
        conda_path = r"C:\ProgramData\anaconda3\Scripts\conda.exe"
        # Construct the command to list packages in the specified environment
        command = [conda_path, 'list', '-n', env_name]
        # Execute the command with shell=True
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        # Check if there were any errors
        if result.stderr:
            print(f"Error: {result.stderr}")
        else:
            print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")
        
from transformers import AutoModel, AutoTokenizer

def download_model(model_name):
    # Load the model and tokenizer from Hugging Face
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def main():
    # Replace 'your_env_name' with the actual name of your Conda environment
    env_name = 'base'
    # list_conda_packages(env_name)
    print("======\n")
    env_name = 'optimum-env'
    # list_conda_packages(env_name)
    
    model_name = "distilbert-base-uncased"
    # model, tokenizer = download_model(model_name)
    print(f"Model {model_name} and tokenizer downloaded successfully!")



if __name__ == "__main__":
    main()

