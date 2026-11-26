---
name: product-compliance
description: >-
  Use when Refaqt places a machine, kit or electrical product on the EU market: CE marking, Machinery Regulation, LVD, EMC, RED, RoHS, REACH, technical file, Declaration of Conformity, test plan, change review.
---
# Product Compliance (CE Marking)

## What it means

To sell a machine or electrical product in the EU, you must show it is safe and carry the CE
mark. The CE mark follows evidence in a technical file. A sticker alone is not enough. Publishing
open-hardware designs does not skip these rules when you place a product on the market.

## The rules

- EU Machinery Regulation (EU) 2023/1230 replaces the Machinery Directive 2006/42/EC. Check the
  current application dates in the official text.
- Often also: EMC Directive 2014/30/EU, Low Voltage Directive (LVD) 2014/35/EU, Radio Equipment
  Directive (RED) for radios, RoHS (restricted substances), REACH (chemicals).
- Harmonized standards give a presumption of conformity: if you follow them, the law treats the
  product as meeting the rule. Common ones: ISO 12100 (risk assessment), ISO 13849-1 or
  IEC 62061 (safety-related control), IEC 60204-1 (electrical equipment of machines), IEC 61010
  (depends on the product).
- Some machine categories need a notified body (an official testing body). Others allow
  self-declaration. The category decides.
- A DIY kit and a finished machine can have different duties. Write down the sales channel.

## What to do next

1. Describe the product and its intended use. List the markets.
2. List each regulation or directive that applies, with the reason.
3. Choose the harmonized standards.
4. Decide: self-declaration or notified body.
5. Build the technical file:
   - [ ] Product description, drawings, BOM revisions
   - [ ] Risk assessment (ISO 12100)
   - [ ] Safety and control concept (ISO 13849 / IEC 62061 if needed)
   - [ ] Electrical schematics and LVD evidence
   - [ ] EMC test reports
   - [ ] Manuals and warnings in the languages of each market
   - [ ] Draft Declaration of Conformity (DoC)
   - [ ] Plan for checks after sale (post-market surveillance)
6. Plan tests (EMC, safety, function) with a test lab. Start at architecture time: late fixes
   cost much more.
7. Map every part in scope: machine, control software, and any connected (IoT) device.
8. Any BOM, firmware or safety-relevant change triggers an impact review before shipment.

Open documentation helps later maintenance. It does not replace the first conformity check.

## When to call a specialist

- **Notified body:** when the category needs one, or when you are unsure.
- **Test lab:** for EMC and electrical safety tests.
- **Lawyer:** for liability, warranty, or a letter from market surveillance.
- A qualified person at Refaqt signs the DoC. Agents never sign it and never claim a product
  complies.

This is guidance, not a conformity assessment.
