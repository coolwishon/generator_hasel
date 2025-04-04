# Hasła Generator 🔒

program Pythona, który generuje losowe hasła o podanej długości liter. On je zapisuje i koduje w pliku .txt
Tworzy zarazem klucz do odkodowania haseł. 

## Opis:
- Hasło zawiera duże/małe litery,cyfry, znaki specjalne.
- Ty decydujesz o  długości hasła tobie odpowiadając 
- Ty podajesz do jakiej witryny owe hasło należy
- Zapisuje hasła w utworzonym przez program pliku dane.txt 
- Koduje zapisane hasła i tworzy klucz dostępny TYLKO DLA UŻYTKOWNIKA key.key
- Program sam pobiera potrzebne biblioteki python

## Jak wygenerować hasło?:
1. Startowanie programu:
    ```
    python main.py
    ```
2. Wprowadź długośc hasła (kod generuje w danej ilości jaką podasz długość hasła)

## Jak odkodować hasło
1. Startowanie odkodowania
    ```
    python decryptor.py
    ```
2. Program wyświetli w konsoli odkodowane hasło

## Zabezpieczenia programu
1. Program posiada key.key za którego użyciem jesteś w stanie odkodować zakodowane generowane hasło, który jako użytkownik możesz zabezpieczyć hasłem. Bez key.key nie jesteś w stanie odkodować hasła. Gdy usuniesz key.key hasła będa zakodowane bez teoretycznie możliwości odkodowania
2. Jesteś w stanie dodać w linijce 62 {generated_password} dzięki czemu wyświetli się ono w konsoli i hacker posiadający wgląd do systemu dostanie informacje w konsoli o treści hasła
3. Jesteś w stanie dodać w linijce 64 i 65 kopiowanie hasła do schowka, które hacker też może przechwycić
        pyperclip.copy(generated_password)
w tym momencie hasło nie wyświetla się w systemie.
 
## Odpowiedzialność
Użytkujesz programu na własną odpowiedzialność. Nie odpowiadam za skradzione hasła. Hackerzy wciąż mogą przechwytywać wpisywane/generowane/kopiowane hasła.
-Szczególnie gdy posiadasz zainfekowany komputer np. keyloggery, spyware, malware
-Są malware które obserwują schowek i kradną hasła gdy je kopiujesz do schowka 
-Jeśli ktoś włamie ci się na komputer na dostęp do pliku dane.txt

## Wymogi
- Python 3.x

## Plany na przyszłośc
