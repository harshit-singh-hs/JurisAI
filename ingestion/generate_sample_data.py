import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

def create_sample_contracts():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    nda_text = """
    NON-DISCLOSURE AGREEMENT
    
    This Non-Disclosure Agreement (the "Agreement") is entered into by and between the Disclosing Party and the Receiving Party.
    
    1. Definition of Confidential Information. "Confidential Information" means any information, technical data, or know-how, including, but not limited to, that which relates to research, product plans, products, services, customers, markets, software, developments, inventions, processes, designs, drawings, engineering, hardware configuration information, marketing, finances, or other business information disclosed by Disclosing Party to Receiving Party, either directly or indirectly in writing, orally, or by inspection of tangible objects.
    
    2. Non-Use and Non-Disclosure. Receiving Party agrees not to use any Confidential Information of Disclosing Party for any purpose except to evaluate and engage in discussions concerning a potential business relationship between the parties. Receiving Party agrees not to disclose any Confidential Information of Disclosing Party to third parties.
    
    3. Maintenance of Confidentiality. Receiving Party agrees that it shall take reasonable measures to protect the secrecy of and avoid disclosure and unauthorized use of the Confidential Information of Disclosing Party.
    
    4. Term. The obligations of Receiving Party under this Agreement shall survive until such time as all Confidential Information of Disclosing Party disclosed hereunder becomes publicly known and made generally available through no action or inaction of Receiving Party.
    """
    
    employment_text = """
    EMPLOYMENT AGREEMENT
    
    This Employment Agreement is made and entered into on this day, between the Employer and the Employee.
    
    1. Position and Duties. The Employer agrees to employ the Employee, and the Employee agrees to be employed by the Employer, as a Software Engineer. The Employee will perform the duties assigned to them by the Employer.
    
    2. Compensation. The Employer shall pay the Employee a base salary of $100,000 per year, payable in accordance with the Employer's standard payroll schedule.
    
    3. At-Will Employment. The Employee's employment with the Employer is "at-will." This means that either the Employee or the Employer may terminate the employment relationship at any time, with or without cause, and with or without notice.
    
    4. Confidentiality. The Employee agrees to keep confidential all proprietary information of the Employer and not to disclose such information to any third party without the Employer's prior written consent.
    
    5. Non-Compete. During the term of employment and for a period of one (1) year thereafter, the Employee agrees not to engage in any business that competes directly with the Employer.
    """
    
    with open(os.path.join(DATA_DIR, "standard_nda.txt"), "w") as f:
        f.write(nda_text)
        
    with open(os.path.join(DATA_DIR, "employment_agreement.txt"), "w") as f:
        f.write(employment_text)
        
    print(f"Created sample contracts in {DATA_DIR}")

if __name__ == "__main__":
    create_sample_contracts()
