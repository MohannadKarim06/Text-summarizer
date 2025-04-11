from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text, max_length, min_length, length_penalty):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summery_ids = model.generate(
        inputs, max_length=max_length, min_length=min_length, length_penalty=length_penalty, num_beams=4
    )
    return tokenizer.decode(summery_ids[0], skip_special_tokens=True)


