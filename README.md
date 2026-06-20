# Laboratorium 05

## Zadanie 1: Przygotowanie lokalnego środowiska
W ramach przygotowania środowiska sworzyłam pliki takie jak:
* `requirements.txt` z niezbędnymi bibliotekami.
* `app.py` z poprzedniego sprawozdania.
* Pliki `Dockerfile` oraz `.dockerignore` konfigurujące obraz


## Zadanie 3
Niestety nie udało mi się zrobić zadania przy użyciu Google Cloud, lecz zamiast teo użyłam Rendera, na którym stworzyłam nowy serwis sieciowy.
<img width="1538" height="107" alt="Zrzut ekranu 2026-06-20 170810" src="https://github.com/user-attachments/assets/9991482c-ee67-40e8-a849-256e44c7b613" />

## Zadanie 4

| Cecha | Serverless | Własny serwer |
| :--- | :--- | :--- |
| **Wdrożenie i konfiguracja** | Szybkie, na podstawie Dockerfile | Trzeba stawiać ręcznie |
| **Zarządzanie** | Bezobsługowe | Pełna odpiowiedzialność użytkownika |
| **Skalowanie** | Automatyczne dopasowywanie zasobów | Zależne od sprzętu |
| **Koszty** | Elastyczne | Stałe koszty zakupu sprzętu i zużycia prądu |
| **Kontrola** | Ograniczona do poziomu aplikacji | Pełna kontrola nad każdą warstwą systemu |


## Zadanie 5
Robiąc zadanie 5 dodałam nową zmienną w Renderze o nazwie MY_API_KEY i przypisałam jej testową wartość. Po zapisaniu zmian Render automatycznie zrestartował aplikację.
<img width="1502" height="261" alt="Zrzut ekranu 2026-06-20 170901" src="https://github.com/user-attachments/assets/9afb1d17-ce92-4369-86e5-c10005202329" />


## Testowanie oraz weryfikacja
Poprawność działania wdrożonego modelu oraz integrację ze zmienną środowiskową sprawdziłam wywołując produkcyjny endpoint `/predict` z wartością.
* <img width="424" height="93" alt="Zrzut ekranu 2026-06-20 171018" src="https://github.com/user-attachments/assets/223c37e1-43b4-4efd-a74d-a36ae6b14bea" />


## Wnioski
Podczas wykonywania sprawozdania zdałam sobię sprawę, jak pomocne i przyjemne jest wdrożenie modelu ML korzystając z usługi serverless. To rozwiązanie pozwala użytkownikowi 
na stworzenie własnego serwisu bez potrzeby długiego "babrania" się w technikaliach tworzenia własnego serwera. Muszę jednak przyznać, że to rozwiązanie jest wyłącznie przydatne
w przypadku, gdy dane nie muszą być kompletnie odizolowane lub gdy nie potrzeba specjalnych wymagań sprzętowych.
