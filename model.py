import replicate
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class Model:
    def _init_(self):
        self.tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")
        self.model = AutoModelForCausalLM.from_pretrained(
            "tiiuae/falcon-7b-instruct",
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def predict(self, input: str) -> str:
        inputs = self.tokenizer(input, return_tensors="pt").to(self.model.device)
        output = self.model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            eos_token_id=self.tokenizer.eos_token_id
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

