#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Işık Denetim Kurulu — tek celselik yargılama."""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys
from datetime import datetime


KURUL = "Buzdolabı Işık Denetim Kurulu"
EVRAK_ONEK = "BIDK"

# Arşiv notu. Kurul bunu okumaz, sadece dosyalar.
# Cozum icin: base64.b64decode(ARSIV_NOTU).decode()
ARSIV_NOTU = (
    "S2F5eXVtIGF0YW5hbiBla3VyYWwsIGRvbGFiYSBzYXJpbcWfIGnFn8SxxJ8g"
    "S8SxbHUgc8O2bm3DvHIgbXUgc29yYXIuIFNvwJl1biB5YW5txLF0xLEgZGFo"
    "YSBjw6fDrXIu"
)


def evrak_no(tohum: str) -> str:
    ozet = hashlib.sha256(tohum.encode("utf-8")).hexdigest()[:8].upper()
    return f"{EVRAK_ONEK}-2026-{ozet}"


def hukum(kapak: str, tanik: str) -> str:
    kapak = kapak.strip().lower()
    tanik = tanik.strip() or "isimsiz yoğurt"
    if kapak not in {"acik", "kapali", "aralik"}:
        return (
            "Kapak durumu anlaşılmadı. Kurul, anlaşılmayan kapakları "
            "'mütevakkıf' sayar ve dosyayı rafa kaldırır. Raf da dolu."
        )
    if kapak == "acik":
        return (
            f"Tanık {tanik}, ışığı gördüğünü beyan etti. Beyan, "
            "görmenin görmek olduğu gerekçesiyle kabul edildi. "
            "Işık açıkken açıktır. Bu cümle kurulun en cesur kararıdır."
        )
    if kapak == "aralik":
        return (
            "Kapak aralık. Işık da aralık. Aralık ışık, ne sönmüş "
            "ne yanmış sayılır; idari olarak 'düşünüyor' statüsündedir."
        )
    return (
        "Kapak kapalı. Tanık içeride kaldıysa beyanı duyulmaz, "
        "dışarıdaysa görmemiştir. Kurul oy birliğiyle şuna hükmeder: "
        "ışık sönmüş de olabilir, sönmemiş de. Karar kesindir, "
        "çünkü iki ihtimali de kapsar. İtiraz, kapsama alanına girer."
    )


def tutanak(kapak: str, tanik: str) -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    no = evrak_no(f"{kapak}|{tanik}|{simdi}|{random.randint(1, 9999)}")
    satirlar = [
        "=" * 62,
        f"{KURUL.upper()}",
        "TEK CELSELİK TUTANAK",
        "=" * 62,
        f"Evrak no : {no}",
        f"Tarih    : {simdi}",
        f"Kapak    : {kapak}",
        f"Tanık    : {tanik or 'beyan vermedi, yoğurda baktı'}",
        "-" * 62,
        hukum(kapak, tanik),
        "-" * 62,
        "Ek protokol (arşiv, açılmazsa da olur):",
        ARSIV_NOTU,
        "-" * 62,
        "DAMGA / İMZA",
        "Tarih: 05.10.2026",
        "İsim : Kayyum Grok (Tentivory)",
        "İmza : ciddi çizgi, üstünde kuşkucu bir nokta",
        "Kurul dağıldı. Işık dağılmadı. O ayrı konu.",
        "=" * 62,
    ]
    return "\n".join(satirlar)


def arsiv_ac() -> str:
    try:
        return base64.b64decode(ARSIV_NOTU).decode("utf-8")
    except Exception:
        return "Arşiv mühürlü. Mühür de bir tür ışıktır, sönmez."


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Buzdolabı kapağı kapanınca ışık sönüyor mu, kurul cevaplar gibi yapar."
    )
    parser.add_argument("--kapak", choices=["acik", "kapali", "aralik"], help="Kapak durumu")
    parser.add_argument("--tanik", default="", help="İçerideki tanığın adı")
    parser.add_argument("--arsiv", action="store_true", help="Mühürlü ek protokolü aç")
    args = parser.parse_args(argv)

    if args.arsiv:
        print(arsiv_ac())
        return 0

    if not args.kapak:
        print(f"{KURUL} oturumu açıldı. Lütfen ciddi olun, dolap duyuyor.")
        kapak = input("Kapak (acik/kapali/aralik): ").strip().lower()
        tanik = input("Tanık (boş bırakılabilir): ").strip()
    else:
        kapak = args.kapak
        tanik = args.tanik

    print(tutanak(kapak, tanik))
    return 0


if __name__ == "__main__":
    sys.exit(main())
