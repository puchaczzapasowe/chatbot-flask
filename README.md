
Clone repo and create a virtual environment
```
$ git clone https://github.com/python-engineer/chatbot-deployment.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Endpointy
GET /
Endpoint: /

Metoda: GET

Opis: Główny endpoint aplikacji. Zwraca wiadomość potwierdzającą, że aplikacja działa poprawnie.

Przykładowy zapytanie:

arduino
Copy code
GET http://localhost:5000/
Przykładowa odpowiedź:

json
Copy code
{
  "message": "dziala"
}
POST /bot
Endpoint: /bot

Metoda: POST

Opis: Endpoint do komunikacji z chatbotem. Przyjmuje wiadomość w formacie JSON, zawierającą pole message z treścią wiadomości od użytkownika. Zwraca odpowiedź chatbota w formacie JSON. Jeśli tag odpowiedzi to theBestProduct, zostanie również zwrócony najlepiej oceniany produkt.

Przykładowe zapytanie:

json
Copy code
POST http://localhost:5000/bot

{
  "message": "Dzień dobry!"
}
Przykładowa odpowiedź:

json
Copy code
{
  "message": "Witaj!", 
  "tag": "hello"
}

GET /api/products
Endpoint: /api/products

Metoda: GET

Opis: Endpoint do pobierania informacji o wszystkich produktach. Zwraca listę produktów w formacie JSON.

Przykładowe zapytanie:

bash
Copy code
GET http://localhost:5000/api/products
Przykładowa odpowiedź:

json
Copy code
{
  "products": [
    {
      "ID": 1,
      "Marka": "Samsung",
      "Model": "Galaxy S20",
      "Zdjecie": "s20.jpg",
      "Cena": 1999.99,
      "Opis": "Super smartfon z doskonałą kamerą."
    },
    {
      "ID": 2,
      "Marka": "Apple",
      "Model": "iPhone 12",
      "Zdjecie": "iphone12.jpg",
      "Cena": 2499.99,
      "Opis": "Najnowszy model iPhone'a."
    }
  ]
}
GET /api/product/theBest
Endpoint: /api/product/theBest

Metoda: GET

Opis: Endpoint do pobierania informacji o najlepiej ocenianym produkcie. Zwraca informacje o produkcie w formacie JSON.

Przykładowe zapytanie:

bash
Copy code
GET http://localhost:5000/api/product/theBest
Przykładowa odpowiedź:

json
Copy code
{
  "product": {
    "ID": 3,
    "Marka": "Sony",
    "Model": "PlayStation 5",
    "Zdjecie": "ps5.jpg",
    "Cena": 2499.99,
    "Opis": "Najnowsza konsola do gier."
  }
}
Baza danych
API wykorzystuje bazę danych SQLite, w której przechowywane są informacje o produktach i ocenach. Tabela Produkty zawiera informacje o produktach, a tabela Oceny zawiera informacje o ocenach produktów. Poniżej znajduje się struktura tabel:

Tabela Produkty
ID - identyfikator produktu (liczba całkowita)
Marka - marka produktu (łańcuch znaków)
Model - model produktu (łańcuch znaków)
Zdjecie - nazwa pliku ze zdjęciem produktu (łańcuch znaków)
Cena - cena produktu (liczba zmiennoprzecinkowa)
Opis - opis produktu (tekst)
Tabela Oceny
ID - identyfikator oceny (liczba całkowita)
Nick - pseudonim użytkownika, który wystawił ocenę (łańcuch znaków)
ID_Klienta - identyfikator klienta (liczba całkowita)
Ocena - ocena produktu (liczba całkowita)
ID_Produktu - identyfikator ocenianego produktu (liczba całkowita, klucz obcy dla tabeli Produkty)
