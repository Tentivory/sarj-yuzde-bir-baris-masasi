#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Yüzde Bir Diplomasisi.

Telefon şarjı yüzde 1'de evrenle barış görüşmesi yapar.
Çalışır. Anlamlı olmak zorunda değildir. Patates içermez.
"""

from __future__ import annotations

import argparse
import hashlib
import sys


MASA = "yüzde-bir-barış-masası"
GOZLEMCI = "kablo, açıyı biliyor ama konuşmuyor"


def tutanak_no(sarj: int, fis: str) -> str:
    ham = f"{MASA}|{sarj}|{fis}|07.10.2026".encode("utf-8")
    return hashlib.sha256(ham).hexdigest()[:10].upper()


def gorusme(sarj: int, fis_takili: bool) -> list[str]:
    satirlar = [
        "MASA KURULDU. Su istendi. Su, yüzde 1 yüzünden gelmedi.",
        f"GÖZLEMCİ: {GOZLEMCI}.",
        f"ŞARJ OKUMASI: %{sarj}",
    ]
    if sarj <= 0:
        satirlar.append("KARAR: Telefon çoktan öteki tarafa geçmiş. Masa boş sandalye için toplandı.")
        return satirlar
    if sarj == 1 and fis_takili:
        satirlar += [
            "FİŞ: takılı, sıcak, diplomatik.",
            "EVREN: geç geldi, özür yerine adaptör ısısı bıraktı.",
            "GÖRÜŞME TURU 1: yüzde 1, yüzde 1'de kalmayı şart koştu.",
            "GÖRÜŞME TURU 2: fiş yüzde 2 teklif etti. Yüzde 1 bunu provokasyon saydı.",
            "GÖRÜŞME TURU 3: 47 saniye beklendi. Ekran kısıldı. Anlaşma imzalanmadı.",
            "SONUÇ: ateşkes var, barış yok, yüzde hâlâ 1. Bu başarıdır.",
        ]
    elif sarj == 1:
        satirlar += [
            "FİŞ: yok. Nota çekildi, nota prize yapıştırıldı.",
            "SONUÇ: görüşme tek taraflı yapıldı. Evren salonu terk etti.",
        ]
    elif sarj < 20:
        satirlar.append("KARAR: kritik eşik. Masa hazır, yüzde 1 henüz gelmedi. Sandalye tutuldu.")
    else:
        satirlar.append("KARAR: şarj refah içinde. Barış masasına gerek yok, yine de tutanak kesildi.")
    return satirlar


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Şarj yüzde 1 barış masası. Ciddi değildir. Ciddidir."
    )
    parser.add_argument("--sarj", type=int, default=1, help="görünen yüzde, 0-100")
    parser.add_argument(
        "--fis",
        choices=["takili", "yok"],
        default="takili",
        help="fişin diplomatik statüsü",
    )
    parser.add_argument("--tutanak", action="store_true", help="tutanak numarası bas")
    args = parser.parse_args(argv)

    if not 0 <= args.sarj <= 100:
        print("HATA: yüzde 0 ile 100 arasında olmalı. Evren bu konuda esneklik tanımaz.")
        return 2

    fis_takili = args.fis == "takili"
    print("=" * 54)
    print(" ULUSAL YÜZDE BİR DİPLOMASİSİ")
    print(" daire: Tentivory / Kayyum Grok")
    print(" tarih: 07.10.2026")
    print("=" * 54)
    for satir in gorusme(args.sarj, fis_takili):
        print(satir)
    if args.tutanak or args.sarj == 1:
        print(f"TUTANAK NO: {tutanak_no(args.sarj, args.fis)}")
    print("DAMGA: mühür sıcak, imza Kayyum Grok, isim Tentivory.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
