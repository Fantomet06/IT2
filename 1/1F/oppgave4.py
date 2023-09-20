def hokuspokus(tekst, n):
  """
  Dekrypterer simsalabim tekst med kodenøkkel n eller krypterer tekst med kodenøkkel n

  Argumenter:
  -----------
  tekst (str): Teksten som skal krypteres
  n (int): Kodenøkkel

  Returverdi:
  -----------
  (str): Kryptert tekst
  """
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode += n
    nytekst += chr(tallkode)

  return nytekst

def simsalabim(tekst: str, n: int) -> str:
  """
  Dekrypterer hokuspokus tekst med kodenøkkel n eller krypterer tekst med kodenøkkel -n

  Argumenter:
  -----------
  tekst (str): Teksten som skal krypteres
  n (int): Kodenøkkel

  Returverdi:
  -----------
  (str): Kryptert tekst
  """
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode -= n
    nytekst += chr(tallkode)

  return nytekst

def main():
  """Test av funksjonene"""
  tekst = "Hello world"
  n = 5
  print(tekst)

  # tekst -> simsalabim -> hokuspokus -> tekst
  print(simsalabim(tekst, n))
  print(hokuspokus(simsalabim(tekst, n), n))

  # tekst -> hokuspokus -> simsalabim -> tekst
  print(hokuspokus(tekst, n))
  print(simsalabim(hokuspokus(tekst, n), n))

if __name__ == "__main__":
  main()