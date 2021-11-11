class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
            #seuraavat rivit koska rikotaan nested blocks sääntöä, sekä max-statements
            if maara >= 41:
                if maara == 42:
                    print("vastaus on 42")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")
                print("maara on 41 tai enemmän...")

        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}, ja tosiaan noin paljon sinne mahtui"
