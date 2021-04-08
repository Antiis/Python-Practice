text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(":")
text_o=text[pos+1:]
text_f=float(text_o.strip())
print(text_f)
