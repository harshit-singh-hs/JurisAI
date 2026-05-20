"""
Generate comprehensive legal procedure and reference documents for the RAG corpus.
Covers: Property Law, Business Law, Criminal Law, Civil Procedure, Family Law,
Consumer Protection, Labour Law, Intellectual Property, Tax Law, Environmental Law,
and common legal procedures in India.
"""
import os

OUTPUT_DIR = "d:/Project/Online-Legal-Advisor/data/legal_corpus"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DOCUMENTS = {
    # ===== PROPERTY LAW =====
    "property_buying_land_procedure.txt": """LEGAL PROCEDURE: BUYING LAND IN INDIA

1. IDENTIFY THE PROPERTY
- Shortlist the property based on location, budget, and purpose (residential, commercial, agricultural).
- Verify the property is not in a restricted zone or notified area.

2. VERIFY OWNERSHIP & TITLE
- Obtain and examine the Title Deed (Sale Deed) of the current owner.
- Conduct a Title Search at the Sub-Registrar's Office for at least the last 30 years.
- Check the Chain of Title to ensure unbroken transfer history.
- Reference: Transfer of Property Act, 1882 (Section 54 - Sale of Immovable Property).

3. CHECK ENCUMBRANCE CERTIFICATE (EC)
- Obtain an Encumbrance Certificate from the Sub-Registrar's office.
- This certifies that the property is free from any legal or monetary liability.
- Typically required for the last 13–30 years.

4. VERIFY LAND USE AND ZONING
- Check the approved land use from the local municipal/development authority.
- Agricultural land requires conversion (NA - Non-Agricultural) before construction.
- Reference: State-specific Land Revenue Codes.

5. CHECK PROPERTY TAX RECEIPTS
- Verify all property tax payments are up to date.
- Obtain copies of recent tax receipts from the local municipal body.

6. OBTAIN NECESSARY APPROVALS
- Building plan approval from municipal corporation (for construction).
- Environmental clearance (for large projects).
- NOC from relevant authorities (Housing Board, Military, Airport Authority, etc.).

7. DRAFT THE SALE AGREEMENT
- Engage a lawyer to draft the Agreement to Sell.
- Include: sale consideration, payment schedule, possession date, penalty clauses.
- Both parties sign; typically involves payment of earnest money (token advance).
- Reference: Indian Contract Act, 1872 (Sections 10, 23, 25).

8. DUE DILIGENCE
- Physical inspection of the property and boundaries.
- Verify property matches revenue records (Khasra, Khatauni, 7/12 extract).
- Check for any ongoing litigation (Lis Pendens - Section 52, Transfer of Property Act).

9. EXECUTE THE SALE DEED
- Draft the Sale Deed on stamp paper of prescribed value.
- Pay Stamp Duty (varies by state, typically 5-8% of property value).
- Pay Registration Fee (typically 1% of property value).
- Reference: Indian Stamp Act, 1899; Registration Act, 1908 (Section 17).

10. REGISTER THE SALE DEED
- Both buyer and seller, along with two witnesses, must appear at the Sub-Registrar's Office.
- Submit biometric data and photographs.
- The Sub-Registrar verifies and registers the deed.

11. MUTATION OF PROPERTY
- Apply for mutation (name transfer) in revenue records at the Tehsildar's office.
- Also update property tax records with the local municipal body.

12. TAKE PHYSICAL POSSESSION
- Take actual possession of the property.
- Obtain a Possession Letter if buying from a developer.

KEY LEGAL REFERENCES:
- Transfer of Property Act, 1882
- Registration Act, 1908
- Indian Stamp Act, 1899
- Indian Contract Act, 1872
- Real Estate (Regulation and Development) Act, 2016 (RERA)
""",

    "property_selling_procedure.txt": """LEGAL PROCEDURE: SELLING PROPERTY IN INDIA

1. PREPARE DOCUMENTS
- Original Sale Deed / Title Deed
- Encumbrance Certificate (last 30 years)
- Property Tax Receipts (up to date)
- Approved Building Plan (if applicable)
- Occupancy Certificate / Completion Certificate
- NOC from Housing Society (if apartment)

2. DETERMINE FAIR MARKET VALUE
- Get the property valued by a registered valuer.
- Check the Circle Rate / Guideline Value set by the state government.
- The sale price cannot be lower than the circle rate for stamp duty purposes.

3. FIND A BUYER
- Engage a real estate agent or list the property.
- Verify the buyer's credentials and financial capability.

4. NEGOTIATE AND SIGN AGREEMENT TO SELL
- Draft an Agreement to Sell with the help of a lawyer.
- Collect earnest money (token amount, typically 10% of sale price).
- Specify timelines, conditions, and penalty for breach.
- Reference: Indian Contract Act, 1872 (Sections 10, 73, 74).

5. OBTAIN NOC AND CLEARANCES
- NOC from the housing society or builder (for apartments).
- Tax clearance certificate from municipal body.
- Mortgage release letter from bank (if property has an outstanding loan).

6. EXECUTE THE SALE DEED
- The Sale Deed is drafted on non-judicial stamp paper.
- Stamp Duty is typically borne by the buyer.
- Both parties sign in the presence of two witnesses.
- Reference: Indian Stamp Act, 1899; Registration Act, 1908.

7. REGISTER THE SALE DEED
- Both parties attend the Sub-Registrar's Office.
- Biometric verification and photograph submission.
- The deed is officially registered and a certified copy is issued.

8. HAND OVER POSSESSION
- Deliver physical possession along with all original documents.
- Provide Possession Letter and all utility transfer documents.

9. CAPITAL GAINS TAX
- Short-term capital gains (held < 2 years): taxed at slab rate.
- Long-term capital gains (held > 2 years): taxed at 20% with indexation.
- Exemptions available under Sections 54, 54EC, 54F of the Income Tax Act, 1961.
- Reference: Income Tax Act, 1961 (Sections 45, 48, 54, 54EC).

10. MUTATION IN REVENUE RECORDS
- The buyer will apply for mutation; the seller may need to provide an affidavit.
""",

    "property_rental_agreement.txt": """LEGAL PROCEDURE: CREATING A RENTAL/LEASE AGREEMENT IN INDIA

1. TYPES OF RENTAL AGREEMENTS
- Leave and License Agreement (recommended, commonly used): Governed by state-specific laws.
- Lease Agreement (for longer terms, typically > 12 months): Governed by Transfer of Property Act, 1882 (Section 105).
- Rent Agreement under Rent Control Acts (state-specific).

2. ESSENTIAL CLAUSES IN A RENTAL AGREEMENT
- Names and addresses of landlord and tenant.
- Description of the property (address, area, furnishing details).
- Monthly rent amount and due date.
- Security deposit amount (typically 2-10 months' rent depending on city).
- Duration of the agreement (11 months is common to avoid Registration Act requirements).
- Notice period for termination (typically 1-3 months).
- Maintenance charges and utility responsibilities.
- Restrictions on subletting and use of premises.
- Clause on rent escalation (annual increase, typically 5-10%).
- Reference: Indian Contract Act, 1872; Transfer of Property Act, 1882.

3. STAMP DUTY AND REGISTRATION
- Agreements for 11 months or less: Stamp duty on notarized agreement (varies by state).
- Agreements exceeding 12 months: Must be registered under Registration Act, 1908 (Section 17).
- E-registration available in many states (Maharashtra, Karnataka, etc.).

4. POLICE VERIFICATION
- Landlord should get police verification of the tenant done.
- Required in many cities; available online in some states.

5. RIGHTS OF LANDLORD
- Right to receive rent on time.
- Right to inspect the property with prior notice.
- Right to evict tenant for non-payment, misuse, or breach of terms.
- Reference: State-specific Rent Control Acts.

6. RIGHTS OF TENANT
- Right to peaceful possession during the lease period.
- Right to essential services (water, electricity).
- Protection against arbitrary eviction.
- Right to receive rent receipts.
- Reference: State-specific Rent Control Acts; Model Tenancy Act, 2021.

7. EVICTION PROCEDURE
- Issue a legal notice to the tenant specifying grounds for eviction.
- If tenant does not vacate, file an eviction petition before the Rent Controller/Court.
- Grounds: Non-payment of rent, subletting without permission, misuse, bona fide need of landlord.
- Reference: State Rent Control Acts; Code of Civil Procedure, 1908 (Order XXI).
""",

    "property_gift_deed.txt": """LEGAL PROCEDURE: GIFT DEED FOR PROPERTY IN INDIA

1. WHAT IS A GIFT DEED?
- A Gift Deed is a legal document that transfers ownership of property from the donor (giver) to the donee (receiver) without any consideration (money).
- Reference: Transfer of Property Act, 1882 (Section 122 - Definition of Gift).

2. ESSENTIAL ELEMENTS
- The transfer must be voluntary, without coercion or undue influence.
- The donor must be competent to contract (major, sound mind).
- The donee must accept the gift during the lifetime of the donor.
- The gift must be of existing property, not future property.
- Reference: Transfer of Property Act, 1882 (Sections 122-129).

3. PROCEDURE
- Draft the Gift Deed on non-judicial stamp paper.
- Pay Stamp Duty (varies by state; often concessional for blood relatives).
- Both donor and donee sign in the presence of two witnesses.
- Register the Gift Deed at the Sub-Registrar's Office (mandatory for immovable property).
- Reference: Registration Act, 1908 (Section 17).

4. TAX IMPLICATIONS
- Gifts from specified relatives (spouse, siblings, parents, etc.) are tax-free.
- Gifts from non-relatives exceeding Rs. 50,000 are taxable in the hands of the donee.
- Reference: Income Tax Act, 1961 (Section 56(2)(x)).

5. REVOCATION OF GIFT
- A gift may be revoked if both parties agree, or if conditions specified in the deed are not fulfilled.
- A gift made under undue influence, coercion, or fraud can be challenged in court.
- Reference: Transfer of Property Act, 1882 (Section 126).
""",

    "property_will_succession.txt": """LEGAL GUIDE: WILLS AND SUCCESSION IN INDIA

1. WHAT IS A WILL?
- A Will is a legal declaration of a person's intention regarding the disposal of their property after death.
- The person making the will is called the Testator.
- Reference: Indian Succession Act, 1925 (Section 2(h), Section 59).

2. WHO CAN MAKE A WILL?
- Any person of sound mind who has attained the age of majority (18 years).
- A Will made under coercion, undue influence, or fraud is void.
- Reference: Indian Succession Act, 1925 (Section 59).

3. HOW TO MAKE A VALID WILL
- The Will must be in writing (handwritten or typed).
- It must be signed by the Testator.
- It must be attested by at least two witnesses who are present when the Testator signs.
- Registration is optional but recommended (at the Sub-Registrar's Office).
- Reference: Indian Succession Act, 1925 (Section 63).

4. TYPES OF WILLS
- Simple Will: Straightforward distribution of assets.
- Conditional Will: Subject to certain conditions being met.
- Joint Will: Made by two or more persons (e.g., husband and wife).
- Holograph Will: Entirely handwritten by the Testator.

5. INTESTATE SUCCESSION (WITHOUT A WILL)
- For Hindus: Hindu Succession Act, 1956 governs. Property distributed among Class I heirs (spouse, sons, daughters, mother).
- For Muslims: Muslim Personal Law applies. Fixed shares for heirs.
- For Christians and Parsis: Indian Succession Act, 1925.
- Reference: Hindu Succession Act, 1956 (Sections 8-16); Indian Succession Act, 1925 (Sections 31-49).

6. PROBATE
- A Probate is a court order certifying the Will as valid.
- Required in some states (West Bengal, Mumbai, Chennai for certain properties).
- Application for Probate is filed in the District Court/High Court.
- Reference: Indian Succession Act, 1925 (Section 213).

7. CHALLENGING A WILL
- A Will can be challenged on grounds of: unsound mind, undue influence, fraud, forgery, improper attestation.
- Limitation period: 12 years from the date the right accrues.
- Reference: Indian Succession Act, 1925; Limitation Act, 1963 (Article 137).
""",

    # ===== BUSINESS LAW =====
    "business_company_registration.txt": """LEGAL PROCEDURE: REGISTERING A COMPANY IN INDIA

1. TYPES OF COMPANIES
- Private Limited Company (Pvt. Ltd.): Minimum 2 directors, 2 shareholders. Most common for startups.
- Public Limited Company (Ltd.): Minimum 3 directors, 7 shareholders. Can list on stock exchange.
- One Person Company (OPC): Single director and shareholder.
- Limited Liability Partnership (LLP): Minimum 2 designated partners.
- Reference: Companies Act, 2013 (Sections 2(68), 2(71), 2(62)); LLP Act, 2008.

2. PRE-REGISTRATION STEPS
- Obtain Digital Signature Certificate (DSC) for all directors.
- Obtain Director Identification Number (DIN) via SPICe+ form.
- Reserve a unique company name via the RUN (Reserve Unique Name) service on MCA portal.

3. INCORPORATION PROCESS (SPICe+ FORM)
- File SPICe+ (Simplified Proforma for Incorporating Company Electronically Plus) on the MCA portal.
- This single form covers:
  - Company incorporation
  - DIN allotment
  - PAN and TAN application
  - GST registration
  - EPFO and ESIC registration
  - Bank account opening request
- Reference: Companies Act, 2013 (Section 7 - Incorporation of Company).

4. DOCUMENTS REQUIRED
- Memorandum of Association (MOA): Objects and scope of the company.
- Articles of Association (AOA): Internal rules and regulations.
- Proof of registered office address.
- Identity and address proof of directors and shareholders.
- Declaration by professionals (CA/CS/Advocate).
- Reference: Companies Act, 2013 (Sections 4, 5, 7).

5. POST-INCORPORATION COMPLIANCE
- Hold the first Board Meeting within 30 days.
- Issue share certificates within 60 days.
- File Declaration of Commencement of Business (INC-20A) within 180 days.
- Appoint a statutory auditor within 30 days.
- Maintain statutory registers (members, directors, charges).
- Annual compliances: Annual Return (MGT-7), Financial Statements (AOC-4), Income Tax Return.
- Reference: Companies Act, 2013 (Sections 12, 92, 96, 137, 139).

6. KEY REGULATORY BODIES
- Ministry of Corporate Affairs (MCA)
- Registrar of Companies (ROC)
- Securities and Exchange Board of India (SEBI) - for public companies
""",

    "business_partnership_deed.txt": """LEGAL GUIDE: PARTNERSHIP FIRMS IN INDIA

1. WHAT IS A PARTNERSHIP?
- A partnership is the relation between persons who have agreed to share profits of a business carried on by all or any of them acting for all.
- Reference: Indian Partnership Act, 1932 (Section 4).

2. PARTNERSHIP DEED - ESSENTIAL CLAUSES
- Name of the firm and nature of business.
- Names, addresses, and contributions of all partners.
- Profit and loss sharing ratio.
- Rights, duties, and obligations of each partner.
- Duration of partnership (at will or for a fixed term).
- Rules for admission, retirement, and expulsion of partners.
- Procedure for dissolution.
- Dispute resolution mechanism (arbitration clause recommended).
- Reference: Indian Partnership Act, 1932 (Sections 11-17).

3. REGISTRATION OF PARTNERSHIP FIRM
- Registration is optional but highly recommended.
- Without registration, partners cannot file suits against each other or third parties in court.
- File application with the Registrar of Firms along with the partnership deed and fees.
- Reference: Indian Partnership Act, 1932 (Sections 56-59).

4. RIGHTS AND DUTIES OF PARTNERS
- Every partner has the right to participate in management.
- Partners must act in good faith and render true accounts.
- A partner must not carry on competing business.
- Reference: Indian Partnership Act, 1932 (Sections 12-16).

5. DISSOLUTION OF PARTNERSHIP
- By agreement, by notice (partnership at will), by court order.
- Compulsory dissolution: insolvency of all partners, illegality of business.
- Settlement of accounts: debts to third parties paid first, then partners' loans, then capital.
- Reference: Indian Partnership Act, 1932 (Sections 40-55).
""",

    "business_gst_registration.txt": """LEGAL PROCEDURE: GST REGISTRATION IN INDIA

1. WHO MUST REGISTER FOR GST?
- Businesses with annual turnover exceeding Rs. 40 lakhs (Rs. 20 lakhs for special category states).
- Businesses with annual turnover exceeding Rs. 20 lakhs for services (Rs. 10 lakhs for special category states).
- Inter-state suppliers (mandatory regardless of turnover).
- E-commerce operators and their sellers.
- Casual taxable persons and non-resident taxable persons.
- Reference: Central Goods and Services Tax Act, 2017 (Section 22).

2. TYPES OF GST REGISTRATION
- Regular: For businesses above the threshold.
- Composition Scheme: For small businesses (turnover up to Rs. 1.5 crores), pay tax at a fixed rate.
- Casual Registration: For occasional or seasonal businesses.
- Reference: CGST Act, 2017 (Sections 22-25, 10).

3. REGISTRATION PROCESS
- Visit the GST Portal (gst.gov.in).
- Fill Part A of Form GST REG-01 (PAN, mobile number, email).
- Receive OTP verification and Temporary Reference Number (TRN).
- Fill Part B with business details, bank account information, and upload documents.
- Submit the application. ARN (Application Reference Number) is generated.
- Verification by the GST officer within 7 working days.
- GSTIN (15-digit GST Identification Number) is issued.
- Reference: CGST Rules, 2017 (Rules 8-12).

4. DOCUMENTS REQUIRED
- PAN card of the business/proprietor.
- Aadhaar card of the proprietor/partners/directors.
- Proof of business registration (MOA, Partnership Deed, etc.).
- Address proof of the principal place of business.
- Bank account statement or cancelled cheque.
- Photograph of the proprietor/partners/directors.
- Authorization letter or board resolution.

5. POST-REGISTRATION OBLIGATIONS
- Issue GST-compliant invoices.
- File monthly/quarterly returns: GSTR-1 (outward supplies), GSTR-3B (summary return).
- File annual return: GSTR-9.
- Maintain proper books of accounts for 6 years.
- Reference: CGST Act, 2017 (Sections 31, 35, 37, 39, 44).
""",

    "business_trademark_registration.txt": """LEGAL PROCEDURE: TRADEMARK REGISTRATION IN INDIA

1. WHAT IS A TRADEMARK?
- A trademark is a mark capable of being represented graphically and distinguishing goods or services.
- Includes: words, logos, symbols, colors, shapes, sounds, or combinations thereof.
- Reference: Trade Marks Act, 1999 (Section 2(zb)).

2. TRADEMARK SEARCH
- Conduct a trademark search on the IP India website (ipindia.gov.in).
- Check for existing identical or similar marks in the same class.
- Recommended to consult a trademark attorney for comprehensive search.

3. FILING THE APPLICATION
- File application (Form TM-A) online on the IP India portal.
- Specify the mark, class of goods/services (Nice Classification, 45 classes).
- Pay the filing fee (Rs. 4,500 for e-filing; Rs. 9,000 for physical filing; 50% discount for startups, small enterprises, and individuals).
- Reference: Trade Marks Act, 1999 (Section 18); Trade Marks Rules, 2017.

4. EXAMINATION
- The Trademark Registrar examines the application within 30-60 days.
- Objections may be raised under absolute or relative grounds.
- Absolute grounds: descriptive, generic, or deceptive marks (Section 9).
- Relative grounds: conflict with prior marks (Section 11).
- If objections are raised, file a response and/or attend a hearing.

5. PUBLICATION IN TRADEMARK JOURNAL
- If accepted, the trademark is published in the Trade Marks Journal.
- Opposition period: 4 months from publication date.
- Any person can file an opposition (Form TM-O) within this period.
- Reference: Trade Marks Act, 1999 (Sections 20, 21).

6. REGISTRATION CERTIFICATE
- If no opposition or opposition is resolved, the trademark is registered.
- Registration certificate is issued.
- Valid for 10 years from the date of filing; renewable indefinitely.
- Reference: Trade Marks Act, 1999 (Sections 23, 25).

7. TRADEMARK INFRINGEMENT
- Using a mark identical or deceptively similar to a registered trademark is infringement.
- Remedies: Injunction, damages, accounts of profits, delivery up of infringing goods.
- Criminal penalties: Imprisonment up to 3 years and/or fine up to Rs. 2 lakhs.
- Reference: Trade Marks Act, 1999 (Sections 29, 103, 104).
""",

    # ===== CRIMINAL LAW =====
    "criminal_fir_procedure.txt": """LEGAL PROCEDURE: FILING AN FIR (FIRST INFORMATION REPORT) IN INDIA

1. WHAT IS AN FIR?
- An FIR is the first formal document recorded by the police when they receive information about a cognizable offence.
- It sets the criminal law machinery in motion.
- Reference: Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS) (Section 173); [Earlier: Code of Criminal Procedure, 1973 (Section 154)].

2. WHO CAN FILE AN FIR?
- Any person can file an FIR, whether or not they are the victim.
- The informant can be a victim, witness, or any person with knowledge of the offence.
- Police are bound to register the FIR for cognizable offences (Supreme Court: Lalita Kumari v. Govt. of UP, 2014).

3. PROCEDURE TO FILE
- Visit the jurisdictional police station (where the offence occurred).
- Provide information about the offence orally or in writing.
- The Station House Officer (SHO) will record the FIR.
- Read the FIR carefully before signing.
- Obtain a free copy of the FIR immediately.
- Reference: BNSS, 2023 (Section 173).

4. ZERO FIR
- If the police station does not have jurisdiction, a Zero FIR can still be filed.
- It will later be transferred to the appropriate police station.
- The police cannot refuse to register a Zero FIR.

5. E-FIR (ONLINE FIR)
- Many states now allow filing FIRs online through their respective police portals.
- Available for certain categories of offences (e.g., vehicle theft, mobile phone theft).
- The complainant may need to visit the police station later for verification.

6. REFUSAL TO REGISTER FIR
- If police refuse to register an FIR, the complainant can:
  a) Send a written complaint to the Superintendent of Police (SP) - BNSS Section 173(4).
  b) File a complaint directly before the Judicial Magistrate - BNSS Section 175.
  c) Approach the High Court under Article 226 of the Constitution.

7. KEY INFORMATION IN AN FIR
- Date, time, and place of occurrence.
- Details of the accused (if known).
- Description of the offence.
- Names of witnesses.
- Details of property stolen or damaged (if applicable).

8. AFTER FILING THE FIR
- Police begin investigation: visit crime scene, collect evidence, record statements.
- Police file a Charge Sheet (if evidence is found) or Closure Report.
- Charge Sheet must be filed within 60 days (for offences punishable up to 3 years) or 90 days (for more serious offences).
- Reference: BNSS, 2023 (Section 193).
""",

    "criminal_bail_procedure.txt": """LEGAL PROCEDURE: BAIL IN INDIA

1. WHAT IS BAIL?
- Bail is the temporary release of an accused person awaiting trial, with a guarantee (bond/surety) that they will appear in court.
- Reference: Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS) (Sections 478-489).

2. TYPES OF BAIL
a) Regular Bail: Applied after arrest, before the appropriate court.
b) Anticipatory Bail: Applied before arrest, to avoid arrest. Filed in Sessions Court or High Court.
c) Interim Bail: Temporary bail granted for a short period pending hearing of the bail application.
d) Default Bail (Statutory Bail): If charge sheet is not filed within the prescribed period (60/90 days).
- Reference: BNSS, 2023 (Sections 478, 482, 483).

3. BAILABLE VS NON-BAILABLE OFFENCES
- Bailable offences: Bail is a matter of right. Police must grant bail at the station.
- Non-bailable offences: Bail is at the discretion of the court. Court considers gravity of offence, likelihood of absconding, tampering with evidence.
- Reference: BNSS, 2023 (Section 478, 479, 480).

4. PROCEDURE FOR APPLYING FOR BAIL
- File a bail application before the appropriate court (Magistrate Court, Sessions Court, or High Court).
- Attach: copy of FIR, arrest memo, grounds for bail.
- The court hears both the accused and the prosecution.
- Court may impose conditions: surrender passport, regular reporting, no contact with witnesses.
- Reference: BNSS, 2023 (Sections 478-483).

5. FACTORS CONSIDERED BY COURT
- Nature and gravity of the offence.
- Criminal antecedents of the accused.
- Possibility of the accused fleeing from justice.
- Possibility of tampering with evidence or influencing witnesses.
- Health and age of the accused.
- Reference: Supreme Court guidelines in various judgments.

6. CANCELLATION OF BAIL
- Prosecution can apply for cancellation if accused violates bail conditions, threatens witnesses, or absconds.
- Reference: BNSS, 2023 (Section 484).
""",

    "criminal_complaint_magistrate.txt": """LEGAL PROCEDURE: FILING A PRIVATE COMPLAINT BEFORE MAGISTRATE IN INDIA

1. WHEN TO FILE A PRIVATE COMPLAINT
- When police refuse to register an FIR.
- For non-cognizable offences (e.g., cheating, defamation, certain fraud cases).
- When the complainant wants to directly approach the court.
- Reference: BNSS, 2023 (Section 175).

2. PROCEDURE
- Draft a written complaint with facts of the offence, details of accused, evidence.
- File the complaint before the Judicial Magistrate First Class (JMFC) having jurisdiction.
- The Magistrate examines the complainant on oath (Section 175(3), BNSS).
- If prima facie case is made out, Magistrate may:
  a) Direct the police to investigate (Section 175(3), BNSS).
  b) Issue process (summons or warrant) against the accused.

3. EXAMINATION OF WITNESSES
- Before issuing process, the Magistrate may examine the complainant's witnesses.
- The Magistrate can also order an inquiry by a police officer.

4. IMPORTANT CONSIDERATIONS
- Limitation period for filing: Generally within 3 years of the offence (for offences punishable up to 3 years).
- No limitation for serious offences (punishable with death, life imprisonment, or > 3 years).
- Reference: BNSS, 2023 (Section 468); Limitation provisions.

5. AFTER PROCESS IS ISSUED
- The accused is served with summons to appear before the court.
- Charges are framed and trial proceeds.
- Both sides present evidence and witnesses.
- Court delivers judgment.
""",

    # ===== CIVIL PROCEDURE =====
    "civil_filing_suit.txt": """LEGAL PROCEDURE: FILING A CIVIL SUIT IN INDIA

1. WHAT IS A CIVIL SUIT?
- A civil suit is a legal proceeding to enforce a right, seek compensation, or obtain relief in disputes between parties (not criminal matters).
- Reference: Code of Civil Procedure, 1908 (CPC).

2. JURISDICTION
- Pecuniary Jurisdiction: Based on the value of the suit.
- Territorial Jurisdiction: Where the defendant resides or cause of action arose.
- Subject Matter Jurisdiction: Certain courts handle specific types of cases.
- Reference: CPC, 1908 (Sections 15-20).

3. DRAFTING THE PLAINT
- The plaint is the written statement of the plaintiff's case.
- Must contain: facts of the case, cause of action, relief sought, jurisdiction details, verification.
- Reference: CPC, 1908 (Order VII).

4. FILING PROCEDURE
- File the plaint in the appropriate court with required court fees.
- Court fees are based on the suit valuation (Court Fees Act, 1870).
- Attach supporting documents, affidavit of verification.
- The plaint is scrutinized by the court registry.

5. SERVICE OF SUMMONS
- After accepting the plaint, the court issues summons to the defendant.
- The defendant must file a Written Statement (defense) within 30 days (extendable to 120 days).
- Reference: CPC, 1908 (Order V - Summons; Order VIII - Written Statement).

6. TRIAL PROCESS
- Framing of Issues: Court identifies disputed points.
- Plaintiff's Evidence: Examination-in-chief, cross-examination, re-examination.
- Defendant's Evidence: Same procedure.
- Final Arguments by both sides.
- Judgment and Decree.
- Reference: CPC, 1908 (Order XIV - Issues; Order XVIII - Evidence).

7. TYPES OF CIVIL SUITS
- Suits for recovery of money (Order XXXVII - Summary Suits for quicker disposal).
- Suits for declaration of rights.
- Suits for specific performance of contracts.
- Suits for injunction (temporary or permanent).
- Suits for partition of property.
- Suits for possession of property.

8. LIMITATION PERIOD
- Suits for recovery of money: 3 years from when the right to sue accrues.
- Suits for possession of immovable property: 12 years.
- Suits for specific performance: 3 years.
- Reference: Limitation Act, 1963 (Schedule - Articles 55, 65, 54).

9. APPEALS
- First Appeal: To the District Court or High Court.
- Second Appeal: To the High Court on substantial questions of law only.
- Special Leave Petition: To the Supreme Court under Article 136 of the Constitution.
- Reference: CPC, 1908 (Sections 96, 100); Constitution of India (Article 136).
""",

    "civil_injunction.txt": """LEGAL GUIDE: INJUNCTIONS IN INDIAN CIVIL LAW

1. WHAT IS AN INJUNCTION?
- An injunction is a judicial order directing a person to do or refrain from doing a particular act.
- Reference: Specific Relief Act, 1963 (Sections 36-42); CPC, 1908 (Order XXXIX).

2. TYPES OF INJUNCTIONS
a) Temporary (Interim) Injunction: Granted during the pendency of a suit to maintain status quo.
b) Permanent Injunction: Granted in the final decree of the suit.
c) Mandatory Injunction: Directs the defendant to perform a positive act.

3. CONDITIONS FOR TEMPORARY INJUNCTION (THREE-PART TEST)
- Prima Facie Case: The plaintiff must show a genuine, arguable case.
- Balance of Convenience: More hardship to the plaintiff if injunction is denied than to the defendant if granted.
- Irreparable Injury: The plaintiff would suffer harm that cannot be compensated by monetary damages.
- Reference: CPC, 1908 (Order XXXIX, Rules 1-2); Dalpat Kumar v. Prahlad Singh (1992) SC.

4. PROCEDURE
- File an application for temporary injunction along with the main suit (or separately).
- Support with affidavit and documentary evidence.
- Court may grant ex-parte injunction in urgent cases (before hearing the other side).
- Reference: CPC, 1908 (Order XXXIX, Rule 3 - Ex-parte injunction).

5. VIOLATION OF INJUNCTION
- Disobedience of an injunction order is punishable as contempt of court.
- The court may order attachment of property, fine, or imprisonment.
- Reference: CPC, 1908 (Order XXXIX, Rule 2A); Contempt of Courts Act, 1971.
""",

    # ===== FAMILY LAW =====
    "family_divorce_procedure.txt": """LEGAL PROCEDURE: DIVORCE IN INDIA

1. TYPES OF DIVORCE
a) Mutual Consent Divorce: Both spouses agree to dissolve the marriage.
b) Contested Divorce: One spouse files for divorce on specific grounds.
- Reference: Hindu Marriage Act, 1955 (Sections 13, 13B); Special Marriage Act, 1954 (Sections 27, 28).

2. GROUNDS FOR CONTESTED DIVORCE (HINDU MARRIAGE ACT)
- Adultery
- Cruelty (physical or mental)
- Desertion for 2 or more continuous years
- Conversion to another religion
- Unsoundness of mind
- Communicable venereal disease
- Renunciation of the world (Sanyasa)
- Not heard alive for 7 or more years
- Additional grounds for wife: Bigamy, rape/sodomy/bestiality by husband
- Reference: Hindu Marriage Act, 1955 (Sections 13(1), 13(2)).

3. MUTUAL CONSENT DIVORCE PROCEDURE
- File a joint petition in the Family Court.
- First Motion: Court records statements of both parties.
- Cooling-off period: 6 months (court may waive in certain circumstances - Supreme Court in Amardeep Singh v. Harveen Kaur, 2017).
- Second Motion: After the cooling period, both parties reaffirm consent.
- Court passes the decree of divorce.
- Reference: Hindu Marriage Act, 1955 (Section 13B).

4. CONTESTED DIVORCE PROCEDURE
- File a petition for divorce in the Family Court (where marriage was solemnized, or where parties last resided together, or where the respondent resides).
- Service of summons on the respondent.
- Respondent files Written Statement.
- Mediation is typically attempted first.
- Trial: Evidence, cross-examination, arguments.
- Judgment and Decree.
- Reference: Hindu Marriage Act, 1955; Family Courts Act, 1984.

5. KEY ISSUES IN DIVORCE
a) Maintenance/Alimony: Interim and permanent maintenance.
   - Reference: Hindu Marriage Act (Section 24, 25); BNSS (Section 144); Hindu Adoptions and Maintenance Act (Section 18).
b) Child Custody: Best interests of the child is the paramount consideration.
   - Reference: Guardians and Wards Act, 1890 (Section 17); Hindu Minority and Guardianship Act, 1956.
c) Division of Property: Governed by personal laws; concept of matrimonial property being evolved by courts.

6. DIVORCE UNDER OTHER PERSONAL LAWS
- Muslim Law: Talaq (by husband), Khula (by wife), Mubarat (mutual), dissolution under Dissolution of Muslim Marriages Act, 1939.
- Christian Law: Indian Divorce Act, 1869.
- Parsi Law: Parsi Marriage and Divorce Act, 1936.
- Special Marriage Act: Applies to inter-faith marriages and civil marriages.
""",

    "family_domestic_violence.txt": """LEGAL GUIDE: PROTECTION FROM DOMESTIC VIOLENCE IN INDIA

1. WHAT IS DOMESTIC VIOLENCE?
- Includes physical abuse, sexual abuse, verbal/emotional abuse, and economic abuse.
- Applies to any woman in a domestic relationship (wife, live-in partner, mother, sister, widow).
- Reference: Protection of Women from Domestic Violence Act, 2005 (PWDVA) (Section 3).

2. WHO CAN FILE A COMPLAINT?
- The aggrieved woman herself.
- Any person on behalf of the aggrieved woman.
- A Protection Officer appointed under the Act.
- Reference: PWDVA, 2005 (Section 4).

3. REMEDIES AVAILABLE
a) Protection Order: Restraining the respondent from committing domestic violence (Section 18).
b) Residence Order: Preventing the respondent from evicting the woman from the shared household (Section 19).
c) Monetary Relief: Compensation for expenses, losses, medical costs, maintenance (Section 20).
d) Custody Order: Temporary custody of children (Section 21).
e) Compensation Order: For injuries and mental torture (Section 22).

4. PROCEDURE
- File a complaint with the Protection Officer, police, or directly before the Magistrate.
- The Magistrate must hear the case within 3 days and dispose of the application within 60 days.
- Court can pass ex-parte interim orders in urgent cases.
- Reference: PWDVA, 2005 (Sections 12-16).

5. PENALTIES
- Breach of a Protection Order is a cognizable, non-bailable offence.
- Punishment: Imprisonment up to 1 year and/or fine up to Rs. 20,000.
- Reference: PWDVA, 2005 (Section 31).
""",

    # ===== CONSUMER PROTECTION =====
    "consumer_complaint_procedure.txt": """LEGAL PROCEDURE: FILING A CONSUMER COMPLAINT IN INDIA

1. WHAT IS A CONSUMER COMPLAINT?
- A complaint filed by a consumer or consumer association regarding defective goods, deficient services, unfair trade practices, or restrictive trade practices.
- Reference: Consumer Protection Act, 2019 (Sections 2(5), 2(6), 35).

2. WHO CAN FILE?
- The consumer themselves.
- Any recognized consumer association.
- Central or State Government.
- Legal heirs or representatives of the consumer.
- Reference: Consumer Protection Act, 2019 (Section 35).

3. WHERE TO FILE (JURISDICTION)
a) District Consumer Disputes Redressal Commission: Claims up to Rs. 1 crore.
b) State Consumer Disputes Redressal Commission: Claims between Rs. 1 crore and Rs. 10 crores.
c) National Consumer Disputes Redressal Commission (NCDRC): Claims exceeding Rs. 10 crores.
- Reference: Consumer Protection Act, 2019 (Sections 34, 47, 58).

4. PROCEDURE
- Draft the complaint with facts, grounds, and relief sought.
- Attach supporting documents: bills, receipts, warranty cards, correspondence, photographs.
- File the complaint in person or through an advocate.
- No court fee is required (nominal fee in some cases).
- E-filing is available through the EDAAKHIL portal (edaakhil.nic.in).

5. TIMELINE
- Complaint must be filed within 2 years from the date of cause of action.
- The Forum must admit or reject the complaint within 21 days.
- After admission, the opposite party files a response within 30 days.
- The Forum should dispose of the complaint within 3 months (5 months if testing is required).
- Reference: Consumer Protection Act, 2019 (Sections 36, 38).

6. REMEDIES AVAILABLE
- Replacement of goods or refund of price.
- Compensation for loss or injury suffered.
- Removal of defects or deficiency.
- Discontinuance of unfair trade practice.
- Adequate costs to the complainant.
- Punitive damages in cases of misleading advertisements.
- Reference: Consumer Protection Act, 2019 (Section 39).

7. APPEALS
- Appeal from District Commission to State Commission within 45 days.
- Appeal from State Commission to National Commission within 30 days.
- Appeal from National Commission to Supreme Court within 30 days.
- Reference: Consumer Protection Act, 2019 (Sections 41, 51, 67).
""",

    # ===== LABOUR LAW =====
    "labour_employment_termination.txt": """LEGAL GUIDE: EMPLOYMENT TERMINATION AND RETRENCHMENT IN INDIA

1. TYPES OF TERMINATION
a) Resignation: Employee voluntarily leaves. Notice period as per contract (typically 1-3 months).
b) Termination by Employer: Can be for cause (misconduct) or without cause (retrenchment).
c) Retrenchment: Termination due to surplus labour (not related to misconduct).
d) Constructive Dismissal: Employee forced to resign due to hostile work environment.

2. TERMINATION FOR CAUSE (MISCONDUCT)
- Employer must conduct a domestic inquiry before termination.
- Steps: Issue show-cause notice, appoint inquiry officer, give opportunity to defend, pass reasoned order.
- Principles of natural justice must be followed (audi alteram partem - hear the other side).
- Reference: Industrial Disputes Act, 1947 (Section 2(oo)); Standing Orders.

3. RETRENCHMENT PROCEDURE
- Applies to establishments with 100+ workers (for prior government approval).
- Last In, First Out (LIFO) principle applies.
- Must give 1 month's written notice (or pay in lieu).
- Must pay retrenchment compensation: 15 days' average wages for every completed year of continuous service.
- Must inform the appropriate government authority.
- Reference: Industrial Disputes Act, 1947 (Section 25F, 25G, 25N).

4. NOTICE PERIOD AND GRATUITY
- Notice period: As per the employment contract or applicable standing orders.
- Gratuity: Employees with 5+ years of service are entitled to gratuity.
- Gratuity = 15 days' wages × years of service (for every completed year).
- Maximum limit: Rs. 20 lakhs.
- Reference: Payment of Gratuity Act, 1972 (Section 4).

5. WRONGFUL TERMINATION REMEDIES
- File a complaint with the Labour Commissioner.
- Raise an industrial dispute under the Industrial Disputes Act, 1947.
- Remedies: Reinstatement with or without back wages, compensation.
- Reference: Industrial Disputes Act, 1947 (Section 2A, 10, 11A).
""",

    # ===== CONTRACTS =====
    "contract_nda_detailed.txt": """LEGAL GUIDE: NON-DISCLOSURE AGREEMENTS (NDA) IN INDIA

1. WHAT IS AN NDA?
- A Non-Disclosure Agreement (also called a Confidentiality Agreement) is a legally binding contract establishing a confidential relationship between parties.
- It protects proprietary information, trade secrets, and sensitive data.
- Reference: Indian Contract Act, 1872 (Sections 10, 23, 27).

2. TYPES OF NDAs
a) Unilateral NDA: One party discloses, the other receives (e.g., employer-employee).
b) Bilateral/Mutual NDA: Both parties share confidential information (e.g., business partnerships, joint ventures).
c) Multilateral NDA: Three or more parties; at least one party discloses.

3. KEY CLAUSES
- Definition of Confidential Information: Clearly specify what is covered (business plans, financial data, customer lists, technical know-how, algorithms, trade secrets).
- Exclusions: Information already publicly available, independently developed, received from third parties, required by law.
- Obligations of the Receiving Party: Non-disclosure, non-use (except for agreed purpose), safeguarding measures.
- Duration: Typically 2-5 years, but trade secrets may be protected indefinitely.
- Return/Destruction of Information: Upon termination or request.
- Remedies for Breach: Injunctive relief, liquidated damages, indemnification.
- Jurisdiction and Governing Law: Specify the courts and applicable law.

4. ENFORCEABILITY IN INDIA
- NDAs are governed by the Indian Contract Act, 1872.
- Reasonable restrictions are enforceable; overly broad or unreasonable restrictions may be void (Section 27 - Agreements in restraint of trade).
- Specific Relief Act, 1963 allows courts to grant injunctions for breach.
- No specific statute governing NDAs; enforcement is contractual.

5. REMEDIES FOR BREACH
- Injunction to prevent further disclosure (Specific Relief Act, 1963).
- Damages for actual loss suffered (Indian Contract Act, Sections 73-75).
- Criminal prosecution may be possible under IT Act, 2000 (Section 72) for breach of confidentiality by service providers.
""",

    "contract_service_agreement.txt": """LEGAL GUIDE: SERVICE AGREEMENTS IN INDIA

1. WHAT IS A SERVICE AGREEMENT?
- A contract between a service provider and a client specifying the terms of service delivery.
- Reference: Indian Contract Act, 1872 (Sections 10, 23).

2. ESSENTIAL CLAUSES
- Scope of Services: Detailed description of services to be provided.
- Duration: Start date, end date, renewal terms.
- Compensation: Payment terms, invoicing, taxes (GST applicability).
- Service Level Agreement (SLA): Performance standards, uptime guarantees, response times.
- Intellectual Property: Ownership of deliverables, pre-existing IP, licenses.
- Confidentiality: NDA provisions for shared information.
- Indemnification: Protection against third-party claims.
- Limitation of Liability: Cap on damages (typically limited to fees paid).
- Termination: Conditions for termination, notice period, consequences.
- Force Majeure: Excusing performance due to unforeseen events.
- Dispute Resolution: Arbitration clause (Arbitration and Conciliation Act, 1996) or jurisdiction.
- Governing Law: Indian law or as agreed by parties.

3. INDEPENDENT CONTRACTOR VS. EMPLOYEE
- Service agreements create an independent contractor relationship, NOT an employment relationship.
- Key differences: control over work, method of payment, provision of tools, exclusivity.
- Misclassification can lead to labor law obligations.

4. STAMP DUTY
- Service agreements may require stamp duty based on the state where executed.
- Reference: Indian Stamp Act, 1899 (varies by state).
""",

    "contract_employment_agreement.txt": """LEGAL GUIDE: EMPLOYMENT AGREEMENTS IN INDIA

1. PURPOSE
- An employment agreement defines the terms and conditions of employment between employer and employee.
- While not always mandatory, it is strongly recommended to prevent disputes.

2. ESSENTIAL CLAUSES
- Job Title and Description: Role, responsibilities, reporting structure.
- Compensation: Salary breakdown (basic, HRA, special allowances), bonus structure, stock options.
- Working Hours: Standard hours, overtime policy, flexible work arrangements.
- Probation Period: Typically 3-6 months; terms for confirmation or termination during probation.
- Leave Policy: Annual leave, sick leave, casual leave, maternity/paternity leave.
- Confidentiality Clause: Protection of employer's trade secrets and proprietary information.
- Non-Compete Clause: Restrictions on joining competitors (generally unenforceable in India under Section 27 of the Indian Contract Act; reasonable restrictions during employment may be upheld).
- Non-Solicitation Clause: Prohibition on soliciting employer's clients or employees.
- Intellectual Property Assignment: All IP created during employment belongs to the employer.
- Termination Clause: Notice period, grounds for termination, severance pay.
- Dispute Resolution: Arbitration or court jurisdiction.

3. KEY STATUTORY PROTECTIONS
- Minimum wages as per Minimum Wages Act, 1948 (or Code on Wages, 2019).
- Payment of Bonus Act, 1965.
- Employees' Provident Funds and Miscellaneous Provisions Act, 1952.
- Employees' State Insurance Act, 1948.
- Maternity Benefit Act, 1961 (26 weeks paid maternity leave).
- Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013.
- Reference: Various labor codes and acts as applicable.

4. RESTRICTIVE COVENANTS
- Non-compete: Post-termination non-compete clauses are generally VOID in India (Section 27, Indian Contract Act, 1872).
- Non-solicitation: May be enforceable if reasonable in scope and duration.
- Garden Leave: Employee is paid but asked not to work during notice period; more enforceable alternative to non-compete.
""",

    # ===== RTI AND GOVERNMENT =====
    "rti_application_procedure.txt": """LEGAL PROCEDURE: FILING AN RTI APPLICATION IN INDIA

1. WHAT IS RTI?
- The Right to Information Act, 2005 empowers every citizen to request information from public authorities.
- Promotes transparency and accountability in government functioning.
- Reference: Right to Information Act, 2005 (Sections 3, 6).

2. WHO CAN FILE?
- Any citizen of India (not available to corporations, societies, etc.).

3. WHAT INFORMATION CAN BE REQUESTED?
- Any information held by a public authority: records, documents, memos, emails, opinions, press releases, contracts.
- Exemptions: National security, sovereignty, trade secrets, cabinet papers, personal privacy.
- Reference: RTI Act, 2005 (Sections 8, 9).

4. PROCEDURE
- Write a simple application addressed to the Public Information Officer (PIO) of the concerned department.
- No specific format required; just state the information needed clearly.
- Pay the application fee: Rs. 10 (for Central Government; varies for state governments).
- BPL cardholders are exempted from fees.
- Submit by post, in person, or online (rtionline.gov.in for Central Government).
- Reference: RTI Act, 2005 (Section 6).

5. TIMELINE
- The PIO must respond within 30 days.
- If the information concerns the life or liberty of a person: 48 hours.
- If the PIO transfers the application to another authority: 5 days for transfer + 30 days.

6. FIRST APPEAL
- If no response within 30 days or unsatisfactory response, file First Appeal.
- File within 30 days before the First Appellate Authority (officer senior to the PIO).
- No fee for first appeal.
- Reference: RTI Act, 2005 (Section 19(1)).

7. SECOND APPEAL
- If dissatisfied with First Appeal, file Second Appeal within 90 days.
- File before the Central Information Commission (CIC) or State Information Commission (SIC).
- The Commission can impose penalties on the PIO for wrongful denial (Rs. 250 per day, up to Rs. 25,000).
- Reference: RTI Act, 2005 (Sections 19(3), 20).
""",

    # ===== CYBER LAW =====
    "cyber_law_basics.txt": """LEGAL GUIDE: CYBER LAW AND IT ACT IN INDIA

1. GOVERNING LEGISLATION
- Information Technology Act, 2000 (IT Act) and IT (Amendment) Act, 2008.
- Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021.
- Digital Personal Data Protection Act, 2023.

2. COMMON CYBER CRIMES AND PUNISHMENTS
a) Hacking (unauthorized access): Imprisonment up to 3 years and/or fine up to Rs. 5 lakhs. Reference: IT Act, Section 66.
b) Identity Theft: Imprisonment up to 3 years and fine up to Rs. 1 lakh. Reference: IT Act, Section 66C.
c) Cheating by Personation using Computer: Imprisonment up to 3 years and fine up to Rs. 1 lakh. Reference: IT Act, Section 66D.
d) Cyber Stalking/Harassment: Publishing obscene material - Imprisonment up to 3 years and fine up to Rs. 5 lakhs. Reference: IT Act, Section 67.
e) Child Pornography: Imprisonment up to 5 years (first offence), up to 7 years (subsequent). Reference: IT Act, Section 67B.
f) Data Breach: Compensation payable as determined by adjudicating officer. Reference: IT Act, Section 43, 43A.

3. REPORTING CYBER CRIME
- File a complaint at the nearest Cyber Crime Police Station.
- File online at the National Cyber Crime Reporting Portal: cybercrime.gov.in.
- Report financial fraud on 1930 helpline.

4. DATA PROTECTION
- Digital Personal Data Protection Act, 2023 (DPDPA):
  - Consent-based processing of personal data.
  - Right to access, correct, and erase personal data.
  - Data fiduciary obligations.
  - Cross-border data transfer restrictions.
  - Penalties up to Rs. 250 crores for violations.

5. E-COMMERCE AND ELECTRONIC CONTRACTS
- Electronic contracts are valid and enforceable (IT Act, Section 10A).
- Digital signatures have the same legal validity as physical signatures (IT Act, Section 5).
- E-records are admissible as evidence (Indian Evidence Act / Bharatiya Sakshya Adhiniyam, Section 65B).
""",

    # ===== ARBITRATION =====
    "arbitration_procedure.txt": """LEGAL GUIDE: ARBITRATION IN INDIA

1. WHAT IS ARBITRATION?
- Arbitration is an alternative dispute resolution (ADR) mechanism where disputes are resolved by an impartial tribunal instead of courts.
- Reference: Arbitration and Conciliation Act, 1996 (A&C Act).

2. TYPES OF ARBITRATION
a) Domestic Arbitration: Both parties are Indian; seat of arbitration is in India.
b) International Commercial Arbitration: One party is foreign; governed by Part I of the A&C Act.
c) Institutional Arbitration: Conducted under institutional rules (e.g., ICC, SIAC, MCIA, DIAC).
d) Ad Hoc Arbitration: Parties manage the process themselves without an institution.

3. ARBITRATION AGREEMENT
- Must be in writing (can be part of a contract or a separate agreement).
- Must clearly express the intention to resolve disputes through arbitration.
- Reference: A&C Act, 1996 (Section 7).

4. PROCEDURE
a) Notice of Arbitration: Claimant sends notice invoking arbitration.
b) Appointment of Arbitrator(s): As per agreement; if parties fail to agree, court appoints (Section 11).
c) Statement of Claim: Claimant files detailed claim with supporting documents.
d) Statement of Defence: Respondent files defence and counterclaim (if any).
e) Hearings: Oral hearings or document-only proceedings.
f) Award: Arbitral tribunal passes a reasoned award.
- Reference: A&C Act, 1996 (Sections 21-31).

5. TIMELINE
- Domestic arbitration: Award must be passed within 12 months (extendable to 18 months by parties).
- Reference: A&C Act, 1996 (Section 29A).

6. CHALLENGING AN AWARD
- Application to set aside: Filed under Section 34 within 3 months.
- Grounds: Incapacity, invalid agreement, lack of notice, beyond scope, composition of tribunal, conflict with public policy.
- Appeal: Under Section 37 to the High Court (limited grounds).
- Reference: A&C Act, 1996 (Sections 34, 37).

7. ENFORCEMENT
- Domestic awards: Enforceable as a decree of court (Section 36).
- Foreign awards: Enforceable under Part II (New York Convention / Geneva Convention).
- Reference: A&C Act, 1996 (Sections 36, 44-52).
""",

    # ===== ENVIRONMENTAL LAW =====
    "environmental_law_basics.txt": """LEGAL GUIDE: ENVIRONMENTAL LAW IN INDIA

1. KEY LEGISLATION
a) Environment Protection Act, 1986 (EPA): Umbrella legislation for environmental protection.
b) Water (Prevention and Control of Pollution) Act, 1974.
c) Air (Prevention and Control of Pollution) Act, 1981.
d) Forest Conservation Act, 1980.
e) Wildlife Protection Act, 1972.
f) National Green Tribunal Act, 2010.

2. ENVIRONMENTAL CLEARANCE
- Required for projects listed in the EIA Notification, 2006.
- Categories: Category A (Central Government clearance via MoEFCC) and Category B (State-level SEIAA).
- Process: Screening, Scoping, Public Consultation, EIA Report, Appraisal, Decision.
- Reference: EPA, 1986; EIA Notification, 2006.

3. NATIONAL GREEN TRIBUNAL (NGT)
- Specialized court for environmental disputes.
- Has jurisdiction over all civil cases involving environmental issues.
- Can award compensation and direct restoration of damaged environment.
- Appeals from NGT go to the Supreme Court.
- Reference: National Green Tribunal Act, 2010.

4. POLLUTER PAYS PRINCIPLE
- The polluter is liable to pay for the environmental damage caused.
- Recognized by the Supreme Court as a fundamental principle.
- Reference: MC Mehta v. Union of India (various judgments); Article 21 of the Constitution.

5. PUBLIC INTEREST LITIGATION (PIL)
- Any citizen can file a PIL for environmental protection.
- Filed directly in the High Court (Article 226) or Supreme Court (Article 32).
- No court fee required.
""",

    # ===== CONSTITUTIONAL RIGHTS =====
    "fundamental_rights_overview.txt": """LEGAL GUIDE: FUNDAMENTAL RIGHTS UNDER THE CONSTITUTION OF INDIA

1. RIGHT TO EQUALITY (ARTICLES 14-18)
- Article 14: Equality before law and equal protection of laws.
- Article 15: Prohibition of discrimination on grounds of religion, race, caste, sex, or place of birth.
- Article 16: Equality of opportunity in matters of public employment.
- Article 17: Abolition of Untouchability.
- Article 18: Abolition of titles (except military and academic distinctions).

2. RIGHT TO FREEDOM (ARTICLES 19-22)
- Article 19: Six freedoms - speech and expression, assembly, association, movement, residence, and profession.
- Article 20: Protection in respect of conviction for offences (no ex-post-facto law, no double jeopardy, no self-incrimination).
- Article 21: Right to life and personal liberty (expanded to include right to livelihood, privacy, education, clean environment, dignity, legal aid).
- Article 21A: Right to education for children aged 6-14 years.
- Article 22: Protection against arrest and detention.

3. RIGHT AGAINST EXPLOITATION (ARTICLES 23-24)
- Article 23: Prohibition of traffic in human beings and forced labor.
- Article 24: Prohibition of employment of children below 14 years in factories/mines/hazardous employment.

4. RIGHT TO FREEDOM OF RELIGION (ARTICLES 25-28)
- Article 25: Freedom of conscience and free profession, practice, and propagation of religion.
- Article 26: Freedom to manage religious affairs.
- Article 27: Freedom from taxation for promotion of any particular religion.
- Article 28: Freedom from religious instruction in educational institutions wholly funded by the state.

5. CULTURAL AND EDUCATIONAL RIGHTS (ARTICLES 29-30)
- Article 29: Protection of interests of minorities.
- Article 30: Right of minorities to establish and administer educational institutions.

6. RIGHT TO CONSTITUTIONAL REMEDIES (ARTICLE 32)
- Article 32: Right to approach the Supreme Court directly for enforcement of Fundamental Rights.
- Five types of writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto.
- Dr. B.R. Ambedkar called Article 32 the "heart and soul of the Constitution."
- High Courts can also issue writs under Article 226.

7. KEY LIMITATIONS
- Fundamental Rights are not absolute; subject to reasonable restrictions.
- Fundamental Rights can be suspended during a National Emergency (Article 352) except Articles 20 and 21.
- Reference: Constitution of India, Part III (Articles 12-35).
""",

    "directive_principles.txt": """LEGAL GUIDE: DIRECTIVE PRINCIPLES OF STATE POLICY (DPSP)

1. WHAT ARE DPSPs?
- Guidelines for the State to follow while making laws and policies.
- Not enforceable by courts, but fundamental in the governance of the country.
- Reference: Constitution of India, Part IV (Articles 36-51).

2. CATEGORIES OF DPSPs

A. SOCIALISTIC PRINCIPLES
- Article 38: State to secure a social order for the promotion of welfare of the people.
- Article 39: Equal right to adequate means of livelihood, equal pay for equal work, prevention of concentration of wealth.
- Article 39A: Free legal aid and equal justice.
- Article 41: Right to work, education, and public assistance in certain cases.
- Article 42: Just and humane conditions of work and maternity relief.
- Article 43: Living wage and decent standard of life for workers.
- Article 43A: Participation of workers in management of industries.

B. GANDHIAN PRINCIPLES
- Article 40: Organization of village panchayats.
- Article 43: Promotion of cottage industries.
- Article 46: Promotion of educational and economic interests of SC/ST and weaker sections.
- Article 47: Prohibition of intoxicating drinks and drugs injurious to health.
- Article 48: Organization of agriculture and animal husbandry, prohibition of cow slaughter.

C. LIBERAL-INTELLECTUAL PRINCIPLES
- Article 44: Uniform Civil Code for all citizens.
- Article 45: Provision for early childhood care and education.
- Article 48A: Protection and improvement of environment and safeguarding forests and wildlife.
- Article 49: Protection of monuments, places, and objects of national importance.
- Article 50: Separation of judiciary from the executive.
- Article 51: Promotion of international peace and security.

3. RELATIONSHIP WITH FUNDAMENTAL RIGHTS
- DPSPs and Fundamental Rights are complementary.
- In case of conflict, Fundamental Rights generally prevail, but laws implementing DPSPs under Article 39(b) and (c) cannot be challenged for violating Articles 14 and 19.
- Reference: Constitution of India, Article 31C; Minerva Mills v. Union of India (1980).
""",

    # ===== LEGAL AID =====
    "legal_aid_india.txt": """LEGAL GUIDE: FREE LEGAL AID IN INDIA

1. CONSTITUTIONAL BASIS
- Article 39A: The State shall ensure that the legal system promotes justice on a basis of equal opportunity, and shall provide free legal aid.
- Article 14: Right to equality.
- Article 21: Right to life includes right to legal aid (Hussainara Khatoon v. State of Bihar, 1979).

2. GOVERNING LAW
- Legal Services Authorities Act, 1987 (LSAA).
- National Legal Services Authority (NALSA) at the national level.
- State Legal Services Authorities (SLSA) at the state level.
- District Legal Services Authorities (DLSA) at the district level.
- Taluk Legal Services Committees at the taluk level.

3. WHO IS ENTITLED TO FREE LEGAL AID?
- Members of Scheduled Castes or Scheduled Tribes.
- Victims of trafficking or bonded labor.
- Women and children.
- Persons with disabilities.
- Persons in custody (including under-trial prisoners).
- Industrial workmen.
- Victims of mass disasters, ethnic violence, caste atrocity, flood, drought, earthquake, or industrial disaster.
- Persons with annual income less than Rs. 3 lakhs (or as specified by the State).
- Reference: LSAA, 1987 (Section 12).

4. HOW TO APPLY
- Visit the nearest DLSA office or Legal Aid Clinic.
- Submit an application for free legal services.
- Attach: Income certificate, identity proof, details of the case.
- NALSA helpline: 15100.
- Online: nalsa.gov.in.

5. SERVICES PROVIDED
- Free legal representation in courts.
- Legal advice and consultation.
- Drafting of legal documents.
- Lok Adalat (People's Court) for amicable settlement.
- Mediation and conciliation services.
- Reference: LSAA, 1987 (Sections 4, 6, 7, 19-22).

6. LOK ADALAT
- A forum where pending or pre-litigation cases are settled amicably.
- Awards of Lok Adalat are deemed to be decrees of a civil court and are final (no appeal).
- No court fee; if court fee was paid, it is refunded.
- Reference: LSAA, 1987 (Sections 19-22).
""",

    # ===== INTELLECTUAL PROPERTY =====
    "copyright_law.txt": """LEGAL GUIDE: COPYRIGHT LAW IN INDIA

1. WHAT IS COPYRIGHT?
- Copyright is the exclusive right to reproduce, publish, perform, or adapt a literary, artistic, musical, dramatic, or cinematographic work.
- Reference: Copyright Act, 1957 (Section 14).

2. WORKS PROTECTED
- Literary works (books, articles, computer programs).
- Musical works (compositions, melodies).
- Artistic works (paintings, sculptures, photographs, architecture).
- Dramatic works (plays, screenplays).
- Cinematograph films.
- Sound recordings.
- Reference: Copyright Act, 1957 (Section 13).

3. DURATION OF COPYRIGHT
- Literary, dramatic, musical, and artistic works: Lifetime of the author + 60 years.
- Cinematograph films and sound recordings: 60 years from the year of publication.
- Government works: 60 years from the year of publication.
- Reference: Copyright Act, 1957 (Sections 22-29).

4. REGISTRATION PROCEDURE
- Registration is optional but advisable (serves as prima facie evidence in court).
- File application (Form XIV) online at copyright.gov.in.
- Fee: Rs. 500 for literary/artistic works; Rs. 2,000 for cinematograph films.
- Waiting period: 30 days for objections.
- Examination by the Registrar of Copyrights.
- Reference: Copyright Act, 1957 (Section 45); Copyright Rules, 2013.

5. FAIR USE (FAIR DEALING)
- Copyright is not infringed by fair dealing for:
  - Private or personal use, research, criticism, review, news reporting, judicial proceedings, education.
- Reference: Copyright Act, 1957 (Sections 52(1)(a)-(zc)).

6. INFRINGEMENT AND REMEDIES
- Civil remedies: Injunction, damages, accounts of profits, delivery up of infringing copies.
- Criminal penalties: Imprisonment (minimum 6 months, up to 3 years) and fine (minimum Rs. 50,000, up to Rs. 2 lakhs).
- Reference: Copyright Act, 1957 (Sections 55, 63).
""",

    "patent_law.txt": """LEGAL GUIDE: PATENT LAW IN INDIA

1. WHAT IS A PATENT?
- A patent is an exclusive right granted for an invention (product or process) that is new, involves an inventive step, and is capable of industrial application.
- Reference: Patents Act, 1970 (Section 2(1)(j), Section 2(1)(ja)).

2. WHAT CAN BE PATENTED?
- New products and processes in any field of technology.
- Must satisfy: Novelty, Inventive Step, Industrial Applicability.
- Reference: Patents Act, 1970 (Sections 2(1)(j), 2(1)(ja), 2(1)(ac)).

3. WHAT CANNOT BE PATENTED (Section 3)?
- Frivolous inventions contrary to natural laws.
- Inventions contrary to public order or morality.
- Mere discoveries of scientific principles or formulations of abstract theories.
- Substances obtained by mere admixture.
- Methods of agriculture or horticulture.
- Computer programs per se (but software with technical application may be patentable).
- Business methods.
- Traditional knowledge.
- Reference: Patents Act, 1970 (Sections 3, 4).

4. PATENT APPLICATION PROCESS
a) File a patent application (provisional or complete specification) at the Indian Patent Office.
b) Publication: Application is published after 18 months (or early publication upon request).
c) Examination: Request for examination must be filed within 48 months.
d) First Examination Report (FER): Patent Office raises objections.
e) Response: Applicant responds to objections within 6 months.
f) Grant or Refusal: Patent is granted if all objections are resolved.
- Reference: Patents Act, 1970 (Sections 7-11A, 12-15, 43).

5. DURATION
- 20 years from the date of filing.
- Annual renewal fees must be paid.
- Reference: Patents Act, 1970 (Section 53).

6. COMPULSORY LICENSING
- Government can grant compulsory license if: patent not available at reasonable price, not meeting public demand, not worked in India.
- Reference: Patents Act, 1970 (Sections 84-92).

7. INFRINGEMENT
- Making, using, selling, or importing a patented invention without permission.
- Remedies: Injunction, damages or accounts of profits, delivery up.
- Reference: Patents Act, 1970 (Sections 104-115).
""",

    # ===== ADDITIONAL IMPORTANT PROCEDURES =====
    "cheque_bounce_procedure.txt": """LEGAL PROCEDURE: CHEQUE BOUNCE (DISHONOUR OF CHEQUE) IN INDIA

1. WHAT IS CHEQUE BOUNCE?
- When a cheque is returned unpaid by the bank due to insufficient funds or other reasons.
- It is a criminal offence under the Negotiable Instruments Act, 1881.
- Reference: Negotiable Instruments Act, 1881 (Section 138).

2. GROUNDS FOR DISHONOUR
- Insufficient funds in the drawer's account.
- Amount exceeds the arrangement with the bank.
- Cheque is post-dated or stale (valid for 3 months from date of issue).
- Signature mismatch, overwriting, or alteration.
- Account closed.
- Stop payment instructions by the drawer.

3. LEGAL PROCEDURE
Step 1: Receive the cheque return memo from the bank (stating the reason for dishonour).
Step 2: Send a legal notice to the drawer within 30 days of receiving the memo.
  - The notice must demand payment of the cheque amount.
Step 3: Wait for 15 days for the drawer to make the payment.
Step 4: If payment is not made within 15 days, file a criminal complaint before the Magistrate within 30 days.
- Reference: NI Act, 1881 (Sections 138, 141, 142).

4. PENALTIES
- Imprisonment up to 2 years.
- Fine up to twice the cheque amount.
- Or both.
- Reference: NI Act, 1881 (Section 138).

5. COMPOUNDING
- The parties can settle the matter at any stage during the proceedings.
- Upon settlement, the case is compounded (withdrawn).
- Reference: NI Act, 1881 (Section 147).

6. INTERIM COMPENSATION
- Court may direct the accused to pay interim compensation (up to 20% of the cheque amount) during the trial.
- Reference: NI Act, 1881 (Section 143A - inserted by 2018 Amendment).
""",

    "pil_procedure.txt": """LEGAL PROCEDURE: PUBLIC INTEREST LITIGATION (PIL) IN INDIA

1. WHAT IS PIL?
- A legal action initiated for the protection of public interest.
- Any citizen can file a PIL, not necessarily the aggrieved party.
- Pioneered by Justice P.N. Bhagwati and Justice V.R. Krishna Iyer.

2. WHERE TO FILE
- Supreme Court: Under Article 32 of the Constitution (for violation of Fundamental Rights).
- High Court: Under Article 226 of the Constitution (for violation of Fundamental Rights or any legal right).
- No court fee required (or minimal fee in some courts).

3. WHO CAN FILE
- Any public-spirited individual or organization.
- The petitioner must not have personal interest or motive.
- Courts reject PILs filed for publicity, political gain, or to settle personal scores.

4. GROUNDS FOR PIL
- Violation of Fundamental Rights of a group or class of people.
- Environmental degradation.
- Consumer protection issues.
- Corruption and abuse of public office.
- Violation of labor laws.
- Bonded labor and child labor.
- Right to education, health, and clean environment.

5. PROCEDURE
- Draft a writ petition (or even a simple letter/postcard to the Chief Justice).
- State the facts, legal grounds, and relief sought.
- File the petition in the appropriate court.
- Court may issue notices and directions to the respondents (government, authorities).
- Court may appoint committees, amici curiae, or commissioners to investigate.

6. LANDMARK PIL CASES
- Hussainara Khatoon v. State of Bihar (1979): Right to speedy trial and free legal aid.
- MC Mehta v. Union of India (various): Environmental protection.
- Vishaka v. State of Rajasthan (1997): Sexual harassment guidelines at workplace.
- Unni Krishnan v. State of AP (1993): Right to education.
""",

    "mediation_conciliation.txt": """LEGAL GUIDE: MEDIATION AND CONCILIATION IN INDIA

1. WHAT IS MEDIATION?
- A voluntary, confidential process where a neutral third party (mediator) helps disputing parties reach a mutually acceptable settlement.
- Reference: Mediation Act, 2023; CPC, 1908 (Section 89).

2. WHAT IS CONCILIATION?
- Similar to mediation, but the conciliator can suggest solutions and propose settlement terms.
- Reference: Arbitration and Conciliation Act, 1996 (Part III, Sections 61-81).

3. WHEN IS MEDIATION USED?
- Civil disputes (property, commercial, family, consumer).
- Courts often refer cases for mediation before proceeding with trial (Section 89, CPC).
- Mandatory in certain commercial disputes under the Mediation Act, 2023.

4. PROCEDURE (MEDIATION ACT, 2023)
- Pre-litigation mediation: Parties must attempt mediation before filing a suit (for certain categories).
- Institutional mediation through recognized Mediation Service Providers.
- Timeline: 120 days (extendable by 60 days with consent).
- Settlement agreement is enforceable as a judgment or decree.
- Reference: Mediation Act, 2023 (Sections 4-9, 27).

5. ADVANTAGES
- Faster than court proceedings.
- Cost-effective.
- Confidential proceedings.
- Parties retain control over the outcome.
- Preserves relationships.

6. ENFORCEABILITY
- Mediated settlement agreements are final and binding.
- They are enforceable as decrees of a civil court.
- No appeal lies against a mediated settlement agreement (except on limited grounds: fraud, corruption, impersonation).
- Reference: Mediation Act, 2023 (Sections 27-29).
""",

    # ===== TAX LAW =====
    "income_tax_basics.txt": """LEGAL GUIDE: INCOME TAX BASICS IN INDIA

1. GOVERNING LAW
- Income Tax Act, 1961.
- Income Tax Rules, 1962.
- Finance Act (annual budget).

2. WHO MUST PAY INCOME TAX?
- Individuals, Hindu Undivided Families (HUF), Partnership Firms, Companies, Association of Persons (AOP), Body of Individuals (BOI).
- Based on residential status: Resident, Non-Resident, Resident but Not Ordinarily Resident.

3. TAX SLABS (INDIVIDUAL - NEW REGIME, AY 2025-26)
- Up to Rs. 3 lakhs: Nil
- Rs. 3-7 lakhs: 5%
- Rs. 7-10 lakhs: 10%
- Rs. 10-12 lakhs: 15%
- Rs. 12-15 lakhs: 20%
- Above Rs. 15 lakhs: 30%
- Standard deduction: Rs. 75,000.
- Reference: Income Tax Act, 1961 (Section 115BAC).

4. HEADS OF INCOME
a) Salary (Section 15-17).
b) Income from House Property (Sections 22-27).
c) Profits and Gains of Business or Profession (Sections 28-44).
d) Capital Gains (Sections 45-55A).
e) Income from Other Sources (Sections 56-59).

5. IMPORTANT DEDUCTIONS (OLD REGIME)
- Section 80C: Up to Rs. 1.5 lakhs (PPF, ELSS, life insurance, tuition fees, home loan principal).
- Section 80D: Medical insurance premiums (Rs. 25,000 self, Rs. 25,000 parents; Rs. 50,000 for senior citizens).
- Section 80E: Education loan interest (no upper limit).
- Section 80G: Donations to charitable institutions.
- Section 24(b): Home loan interest (up to Rs. 2 lakhs for self-occupied property).

6. FILING INCOME TAX RETURNS
- Due date: 31st July for individuals (non-audit cases).
- File online at incometax.gov.in.
- Forms: ITR-1 (salaried individuals), ITR-2 (capital gains), ITR-3 (business income), ITR-4 (presumptive taxation).
- Reference: Income Tax Act, 1961 (Section 139).

7. PENALTIES
- Non-filing: Penalty up to Rs. 5,000 (Section 234F).
- Under-reporting income: 50% of tax payable (Section 270A).
- Tax evasion: Prosecution and imprisonment (Sections 276C, 277).
""",
}

def generate_files():
    count = 0
    for filename, content in DOCUMENTS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())
        count += 1
        print(f"Created: {filename}")
    print(f"\nGenerated {count} legal procedure/reference documents.")

if __name__ == "__main__":
    generate_files()
