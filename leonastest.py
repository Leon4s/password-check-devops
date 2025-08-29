import password_checker


def check_password(pw: str, expected: bool = True):
    """Hilfsfunktion zum Testen einzelner Passwörter"""
    result = password_checker.is_valid_password(pw)
    assert result == expected, f"Fehler bei Passwort: {pw} (erwartet {expected}, bekommen {result})"


def test_passwords():
    # ✅ Gültige Passwörter
    check_password("Passwort1", True)        # Groß, klein, Zahl, >= 8 Zeichen
    check_password("AbcdefG1", True)         # Exakt 8 Zeichen
    check_password("LangePasswort123", True) # Längeres Passwort
    check_password("XyZ12345", True)         # Mischform

    # ❌ Ungültige Passwörter
    check_password("kurz1A", False)     # Zu kurz (< 8)
    check_password("abcdefgh", False)   # Nur Kleinbuchstaben
    check_password("ABCDEFGH", False)   # Nur Großbuchstaben
    check_password("12345678", False)   # Nur Zahlen
    check_password("Passwort", False)   # Ohne Zahl
    check_password("1234abcd", False)   # Ohne Großbuchstaben
    check_password("1234ABCD", False)   # Ohne Kleinbuchstaben


if __name__ == "__main__":
    try:
        test_passwords()
        print("✅ Alle Tests erfolgreich bestanden!")
    except AssertionError as e:
        print("⚠️  Mindestens ein Test ist fehlgeschlagen.")
        print(e)
        raise
