transcription_dict = {
  "G": "C",
  "C": "G",
  "T": "A",
  "A": "U"
}

def to_rna(seq):
  seq_list = list(seq)
  transcribed = ""
  for x in seq_list:
    if x in transcription_dict.keys(): 
      transcribed += transcription_dict[x]
    else:
      transcribed = ""
      break
  return transcribed
    
