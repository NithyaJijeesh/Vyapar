from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
# Create by athul.


class payment_terms(models.Model):
    payment_terms_number = models.IntegerField(null=True,blank=True)  
    payment_terms_value = models.CharField(max_length=100,null=True,blank=True) 
    days = models.CharField(max_length=100,null=True,blank=True) 


class Distributors_details(models.Model):  
  user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
  distributor_id = models.CharField(max_length=100,null=True,blank=True)
  contact = models.CharField(max_length=255,null=True,blank=True)
  img = models.ImageField(null=True,blank = True,upload_to = 'image/distributor') 
  payment_term =  models.ForeignKey(payment_terms, on_delete=models.CASCADE,null=True,blank=True)
  start_date = models.DateField(max_length=255,null=True,blank=True)
  End_date = models.DateField(max_length=255,null=True,blank=True)
  Log_Action = models.IntegerField(null=True,default=0)

class company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    Distributors = models.ForeignKey(Distributors_details, on_delete=models.CASCADE,null=True,blank=True)
    Company_code = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    pan_number = models.CharField(max_length=255,null=True,blank=True)
    dateperiod=  models.ForeignKey(payment_terms, on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateField(max_length=255,null=True,blank=True)
    End_date = models.DateField(max_length=255,null=True,blank=True)
    gst_type = models.CharField(max_length=255,null=True,blank=True)
    gst_no = models.CharField(max_length=255,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank = True,upload_to = 'image/patient')
    superadmin_approval = models.IntegerField(null=True,default=0)  
    Distributor_approval = models.IntegerField(null=True,default=0) 
    reg_action = models.CharField(max_length=255,null=True,blank=True,default='self')
    

class staff_details(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    user_name = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    img = models.ImageField(null=True,blank = True,upload_to = 'image/staff')    
    Action = models.IntegerField(null=True,default=0)    
    position = models.CharField(max_length=255,null=True,blank=True,default='staff')

class modules_list(models.Model): 
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True) 
    sales_invoice = models.CharField(max_length=100,null=True,default=0)   
    Estimate = models.IntegerField(null=True,default=0)
    Payment_in = models.IntegerField(null=True,default=0) 
    sales_order = models.IntegerField(null=True,default=0)     
    Delivery_challan = models.IntegerField(null=True,default=0) 
    sales_return = models.IntegerField(null=True,default=0) 

    Purchase_bills = models.IntegerField(null=True,default=0)   
    Payment_out = models.IntegerField(null=True,default=0)  
    Purchase_order = models.IntegerField(null=True,default=0)   
    Purchase_return = models.IntegerField(null=True,default=0)  

    Bank_account = models.IntegerField(null=True,default=0)   
    Cash_in_hand = models.IntegerField(null=True,default=0)  
    cheques = models.IntegerField(null=True,default=0)   
    Loan_account = models.IntegerField(null=True,default=0) 
    Upi = models.IntegerField(null=True,default=0) 

    update_action = models.IntegerField(null=True,default=0) 
    status = models.CharField(max_length=100,null=True,default='New')      

#_______________Parties(new)_____________Antony Tom_______

class party(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    party_name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    gst_type = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    openingbalance = models.CharField(max_length=100,default='0',null=True,blank=True)
    payment = models.CharField(max_length=100,null=True,blank=True)
    creditlimit = models.CharField(max_length=100,default='0',null=True,blank=True)
    current_date = models.DateField(max_length=255,null=True,blank=True)
    End_date = models.CharField(max_length=255,null=True,blank=True)
    additionalfield1 = models.CharField(max_length=100,null=True,blank=True)
    additionalfield2 = models.CharField(max_length=100,null=True,blank=True)
    additionalfield3 = models.CharField(max_length=100,null=True,blank=True)
    balance = models.CharField(max_length=100,default='0',null=True,blank=True)

    
#End

# ========================= ASHIKH V U (START)===========================

class ItemModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    item_name = models.CharField(max_length=255)
    item_hsn = models.PositiveIntegerField(null=True)
    item_unit = models.CharField(max_length=255)
    item_taxable = models.CharField(max_length=255)
    item_gst = models.CharField(max_length=255,null=True)
    item_igst = models.CharField(max_length=255,null=True)
    item_sale_price = models.PositiveIntegerField()
    item_purchase_price = models.PositiveBigIntegerField()
    item_opening_stock = models.PositiveBigIntegerField(default=0)
    item_current_stock = models.PositiveBigIntegerField(default=0)
    item_at_price = models.PositiveBigIntegerField(default=0)
    item_date = models.DateField()
    item_min_stock_maintain = models.PositiveBigIntegerField(default=0)

class UnitModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    unit_name = models.CharField(max_length=255)

class TransactionModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(ItemModel,on_delete=models.CASCADE,null=True,blank=True)
    trans_type = models.CharField(max_length=255)
    trans_invoice = models.PositiveBigIntegerField(null=True,blank=True)
    trans_user_name = models.CharField(max_length=255)
    trans_date = models.DateTimeField()
    trans_qty = models.PositiveBigIntegerField(default=0)
    trans_current_qty = models.PositiveBigIntegerField(default=0)
    trans_adjusted_qty = models.PositiveBigIntegerField(default=0)
    trans_price = models.PositiveBigIntegerField(default=0)
    trans_status = models.CharField(max_length=255)
    trans_created_date = models.DateTimeField(auto_now_add=True,null=True)


class BankModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    bank_name = models.CharField(max_length=255)
    account_num = models.PositiveBigIntegerField(null=True)
    ifsc = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    upi_id = models.CharField(max_length=255)
    as_of_date = models.DateField(null=True)
    card_type = models.CharField(max_length=255)
    open_balance = models.BigIntegerField(null=True)
    current_balance = models.BigIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255,null=True)
    
    
class BankTransactionModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    from_here = models.ForeignKey(BankModel,related_name='from_this_bank',on_delete=models.CASCADE,null=True,blank=True)
    to_here = models.ForeignKey(BankModel,related_name='to_this_bank',on_delete=models.CASCADE,null=True,blank=True)
    type = models.CharField(max_length=255,null=True)
    name = models.CharField(max_length=255,null=True)
    date = models.DateField(null=True)
    amount = models.BigIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    transfer_type=models.CharField(max_length=255,null=True)
    current_amount = models.BigIntegerField(default=0)
    last_action = models.CharField(max_length=255,null=True)
    by = models.CharField(max_length=255,null=True) 
    
    
class BankTransactionHistory(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    bank = models.ForeignKey(BankModel,on_delete=models.CASCADE,blank=True,null=True)
    bank_trans = models.ForeignKey(BankTransactionModel,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    action = models.CharField(max_length=255)
    done_by = models.ForeignKey(staff_details,related_name='done_by_staff',on_delete=models.CASCADE,blank=True,null=True)
    done_by_name = models.CharField(max_length=255)

# ========================= ASHIKH V U (END)===========================
class PurchaseBill(models.Model):
    billno = models.IntegerField(default=0,null=True,blank=True)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE)
    billdate = models.DateField()
    duedate = models.DateField(null=True,blank=True)
    supplyplace = models.CharField(max_length=100, default='')
    pay_method = models.CharField(max_length=255, default='', null=True)
    cheque_no = models.CharField(max_length=255, default='', null=True)
    upi_no = models.CharField(max_length=255, default='', null=True)
    subtotal = models.IntegerField(default=0, null=True)
    igst = models.CharField(max_length=100,default=0, null=True)
    cgst = models.CharField(max_length=100,default=0, null=True)
    sgst = models.CharField(max_length=100,default=0, null=True)
    taxamount = models.CharField(max_length=100,default=0, null=True)
    adjust = models.CharField(max_length=100,default=0, null=True)
    grandtotal = models.FloatField(default=0, null=True)
    advance=models.CharField(null=True,blank=True,max_length=255)
    balance=models.CharField(null=True,blank=True,max_length=255)
    tot_bill_no = models.IntegerField(default=0, null=True)

class PurchaseBillItem(models.Model):
    purchasebill = models.ForeignKey(PurchaseBill,on_delete=models.CASCADE)
    company = models.ForeignKey(company,on_delete=models.CASCADE)
    product = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, null=True)
    total = models.IntegerField(default=0, null=True)
    tax = models.CharField(max_length=100)
    discount = models.CharField(max_length=100,default=0, null=True)

class PurchaseBillTransactionHistory(models.Model):
    purchasebill = models.ForeignKey(PurchaseBill,on_delete=models.CASCADE)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
    ]
    action = models.CharField(max_length=20, choices=CHOICES)
    transactiondate = models.DateField(auto_now=True)


    
    
# ==============delivery challan & Estimate ============shemeem --start=======



class DeletedEstimate(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    ref_no = models.CharField(max_length=50)


class DeletedDeliveryChallan(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    challan_no = models.CharField(max_length=50)

# ==================================shemeem --end =======================================

# _____________________SalesInvoice_______________Antony Tom____________

class SalesInvoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    staff = models.ForeignKey(staff_details, on_delete=models.CASCADE,null=True,blank=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE,null=True,blank=True)
    party_name = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    invoice_no = models.IntegerField(default=0,null=True,blank=True)
    date = models.DateField()
    state_of_supply = models.CharField(max_length=255,null=True,blank=True)
    paymenttype = models.CharField(max_length=255,null=True,blank=True)
    cheque = models.CharField(max_length=255,null=True,blank=True)
    upi = models.CharField(max_length=255,null=True,blank=True)
    accountno = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(max_length=255,null=True,blank=True)
    subtotal = models.CharField(max_length=100,default=0, null=True)
    igst = models.CharField(max_length=100,default=0, null=True)
    cgst = models.CharField(max_length=100,default=0, null=True)
    sgst = models.CharField(max_length=100,default=0, null=True)
    total_taxamount = models.CharField(max_length=100,default=0)
    adjustment = models.CharField(max_length=100,default=0, null=True)
    grandtotal = models.FloatField(default=0, null=True)
    paidoff = models.CharField(null=True,blank=True,max_length=255)
    totalbalance = models.CharField(null=True,blank=True,max_length=255)


    
class SalesInvoiceItem(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    staff = models.ForeignKey(staff_details, on_delete=models.CASCADE,null=True,blank=True)
    salesinvoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE,null=True,blank=True)
    hsn = models.IntegerField(default=0,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,null=True,blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,null=True,blank=True)
    tax =  models.CharField(max_length=255,null=True,blank=True)
    totalamount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00,null=True,blank=True)


class SalesInvoiceTransactionHistory(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    salesinvoice = models.ForeignKey(SalesInvoice,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    action = models.CharField(max_length=255)
    done_by_name = models.CharField(max_length=255)
    
#End

# ========================= HARIPRIYA B NAIR (START)===========================
class purchasedebit(models.Model):
    pdebitid = models.AutoField(('pdid'), primary_key=True)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE,null=True,blank=True)
    reference_number=models.TextField(max_length=100,null=True,blank=True)
    debitdate = models.DateField(null=True)
    billno = models.CharField(max_length=150,null=True)
    billdate = models.CharField(max_length=100,null=True)
    supply = models.CharField(max_length=150,null=True)
    subtotal = models.CharField(max_length=100,null=True)
    sgst = models.CharField(max_length=100,null=True)
    cgst = models.CharField(max_length=100,null=True)
    igst = models.CharField(max_length=100,null=True)
    taxamount = models.CharField(max_length=100,null=True)
    grandtotal = models.CharField(max_length=100,null=True)
    adjustment = models.FloatField(default=0,null=True,blank=True)
    paid_amount = models.FloatField(blank=True,null=True)
    balance_amount = models.FloatField(blank=True,null=True)
    payment_type = models.CharField(max_length=100,null=True)
    cheque_no = models.CharField(max_length=255, default='', null=True)
    upi_no = models.CharField(max_length=255, default='', null=True)
    tot_debt_no = models.IntegerField(default=0, null=True)
  


class purchasedebit1(models.Model):
    pdebit = models.ForeignKey(purchasedebit, on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(ItemModel,on_delete=models.CASCADE,null=True)
    qty = models.IntegerField(default=0, null=True)
    total = models.IntegerField(default=0, null=True)
    tax = models.CharField(max_length=100,null=True)
    discount = models.IntegerField(default=0, null=True)


class DebitnoteTransactionHistory(models.Model):
    debitnote = models.ForeignKey(purchasedebit,on_delete=models.CASCADE)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
    ]
    action = models.CharField(max_length=20, choices=CHOICES)
    transactiondate = models.DateField(auto_now=True)



# ========================= HARIPRIYA B NAIR (END)===========================


# Athul -----expense---start
class Expense_Category(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    expense_category = models.CharField(max_length=200)

class Expense(models.Model):  
    staff_id = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)  
    party_id = models.ForeignKey(party,on_delete=models.CASCADE,blank=True,null=True) 
    expense_category_id = models.ForeignKey(Expense_Category,on_delete=models.CASCADE,blank=True,null=True)
    Sub_total = models.FloatField(default='')
    cgst = models.FloatField(default='')
    sgst = models.FloatField(default='')
    tax_amount = models.FloatField(default='')
    adjustment = models.FloatField(default='')
    total = models.FloatField(default='')
    paid = models.FloatField(default='')
    balance = models.FloatField(default='')
    payment_type = models.CharField(max_length=200,default='')
    expense_date = models.DateField(auto_now_add=True,auto_now=False,null=True)
    EXP_NO = models.IntegerField(default=0)
    action = models.IntegerField(default=0)

class Expense_list(models.Model):  
    expense_id = models.ForeignKey(Expense,on_delete=models.CASCADE,blank=True,null=True) 
    discription = models.CharField(max_length=255)
    tax = models.FloatField(default='')
    amount = models.FloatField(default='')


# Athul -----expense---end    

class PurchaseOrder(models.Model):
    orderno = models.IntegerField(default=0,null=True,blank=True)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True,default='')
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True,default='')
    party = models.ForeignKey(party, on_delete=models.CASCADE,default='')
    orderdate = models.DateField(default='')
    duedate = models.DateField(default='')
    supplyplace = models.CharField(max_length=100, default='')
    pay_method = models.CharField(max_length=255, default='', null=True)
    cheque_no = models.CharField(max_length=255, default='', null=True)
    upi_no = models.CharField(max_length=255, default='', null=True)
    subtotal = models.IntegerField(default=0, null=True)
    igst = models.CharField(max_length=100,default=0, null=True)
    cgst = models.CharField(max_length=100,default=0, null=True)
    sgst = models.CharField(max_length=100,default=0, null=True)
    taxamount = models.CharField(max_length=100,default=0, null=True)
    adjust = models.CharField(max_length=100,default=0, null=True)
    grandtotal = models.FloatField(default=0, null=True)
    advance=models.CharField(null=True,blank=True,max_length=255)
    balance=models.CharField(null=True,blank=True,max_length=255)
    tot_ord_no = models.IntegerField(default=0, null=True)
    convert = models.IntegerField(default=0)
    convert_id = models.ForeignKey(PurchaseBill,on_delete=models.CASCADE, null=True,blank=True)
    
    
class PurchaseOrderItem(models.Model):
    purchaseorder = models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE)
    company = models.ForeignKey(company,on_delete=models.CASCADE)
    product = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, null=True)
    total = models.IntegerField(default=0, null=True)
    discount = models.CharField(max_length=100,default=0, null=True)
    
    
class PurchaseOrderTransactionHistory(models.Model):
    purchaseorder = models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
    ]
    action = models.CharField(max_length=20, choices=CHOICES)
    transactiondate = models.DateField(auto_now=True)
    
    
# ========================= nasneen o m ===========================

class salesorder(models.Model):

    party = models.ForeignKey(party, on_delete=models.CASCADE,null=True,blank=True)
    partyname = models.CharField(max_length=100,null=True)
    staff = models.ForeignKey(staff_details, on_delete=models.CASCADE,null=True,blank=True)
    comp = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    orderno = models.IntegerField(null=True)
    orderdate = models.DateField(null=True)
    duedate = models.DateField(null=True)
    
    placeofsupply = models.CharField(max_length=100,null=True)
    payment_method = models.CharField(max_length=100, default='cash')
    UPI = models.CharField(max_length=100,null=True)
    checkno = models.CharField(max_length=100,null=True)
    accno = models.CharField(max_length=100,null=True)
    subtotal = models.CharField(max_length=100,null=True)
    IGST = models.CharField(max_length=100,null=True)
    CGST  =  models.CharField(max_length=100,null=True)
    SGST =  models.CharField(max_length=100,null=True)
    taxamount = models.CharField(max_length=100,null=True)
    adjustment = models.CharField(max_length=100,null=True)
    grandtotal = models.CharField(max_length=100,null=True)

    note = models.TextField(null=True)
    
    paid = models.CharField(max_length=100,null=True)
    balance = models.CharField(max_length=100,null=True)
    
    file = models.FileField(upload_to='sales',null=True)
    status = models.CharField(max_length=100,default='open')
    action = models.CharField(max_length=100,default='convert to invoice')

    @classmethod
    def next_orderno(cls, company_id):
        last_orderno = cls.objects.filter(comp_id=company_id).aggregate(Max('orderno'))['orderno__max']
        return 1 if last_orderno is None else last_orderno + 1
    
class Estimate(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE,null=True)
    sales_order = models.ForeignKey(salesorder, on_delete=models.CASCADE,null=True)
    ref_no = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True, blank=True)
    party_name = models.CharField(max_length=150)
    contact = models.CharField(max_length=255,null=True,blank=True)
    billing_address = models.TextField()
    state_of_supply = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    subtotal = models.FloatField(null=True, blank=True)
    igst = models.FloatField(null=True,blank=True)
    cgst = models.FloatField(null=True,blank=True)
    sgst = models.FloatField(null=True,blank=True)
    tax_amount =  models.FloatField(null=True,blank=True)
    adjustment = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    balance = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True)
    is_converted = models.BooleanField(null=True, default=False)    

class Estimate_items(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    eid = models.ForeignKey(Estimate, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200)
    hsn = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(null=True, blank=True)
    tax = models.CharField(max_length=10)
    discount = models.FloatField(null=True,blank=True)
    total = models.FloatField()
    
class sales_item(models.Model):
    sale_order= models.ForeignKey(salesorder,on_delete=models.CASCADE,null=True)
    cmp = models.ForeignKey(company, on_delete=models.CASCADE,default='')
    # product1 = models.CharField(max_length=100,null=True)
    product= models.ForeignKey(ItemModel,on_delete=models.CASCADE,null=True)

    hsn = models.CharField(max_length=100,null=True)
    # description = models.CharField(max_length=100, default='')
    qty = models.IntegerField(default=0, null=True)
    price = models.CharField(max_length=100,null=True)
    total = models.IntegerField(default=0, null=True)
    discount = models.CharField(max_length=100,null=True)
    tax = models.CharField(max_length=100,null=True)
    taxamount = models.CharField(max_length=100,null=True)

class EstimateTransactionHistory(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    estimate = models.ForeignKey(Estimate,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(auto_now_add=True,auto_now=False,null=True)
    action = models.CharField(max_length=255)    

class saleorder_transaction(models.Model):
    sales_order = models.ForeignKey(salesorder,on_delete=models.CASCADE,blank=True,null=True)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    action = models.CharField(max_length=255,null=True)
    date = models.DateField(null=True)
    
#End

# ==============Anuvinda K V ============payment out=======
class PaymentOut(models.Model):
    purchase=models.ForeignKey(PurchaseBill,on_delete=models.CASCADE,null=True,blank=True)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE)
    billno = models.IntegerField(default=0,null=True,blank=True)
    billdate = models.DateField()
    duedate = models.DateField(null=True,blank=True)
    pay_method = models.CharField(max_length=255, default='', null=True)
    cheque_no = models.CharField(max_length=255, default='', null=True)
    upi_no = models.CharField(max_length=255, default='', null=True)
    balance=models.CharField(null=True,blank=True,max_length=255)
    tot_bill_no = models.IntegerField(default=0, null=True)
    ref_no = models.IntegerField(default=0, null=True, blank=True)
    def paymentout_history(self):
        return PaymentOutHistory.objects.filter(paymentout=self).order_by('-timestamp')
    def paymentout_details(self):
        return self.paymentoutdetails_set.all()
        
class PaymentOutDetails(models.Model):
    paymentout = models.ForeignKey('PaymentOut',on_delete=models.CASCADE,null=True,blank=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    description = models.TextField(null=True)
    files = models.FileField(upload_to='paymentout_files/', null=True, blank=True)

    def __str__(self):
        return str(self.paymentout) 

class PaymentOutHistory(models.Model):
    paymentout = models.ForeignKey(PaymentOut, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)  # 'created' or 'updated'
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add any additional fields you want to track in the history

    def __str__(self):
        return f"{self.paymentout.billno} - {self.action} - {self.timestamp}"
#End

# ==============Payment In============shemeem=============================

class PaymentIn(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE,null=True)
    rec_no = models.BigIntegerField(null=True)
    date = models.DateField(null=True, blank=True)
    party_name = models.CharField(max_length=150)
    contact = models.CharField(max_length=255,null=True,blank=True)
    billing_address = models.TextField()
    description = models.TextField()
    payment_type = models.CharField(max_length=200, null=True, blank=True,default="")
    payment_method = models.CharField(max_length=100, null=True)
    payment_acc_number = models.BigIntegerField(null=True)
    payment_cheque_id = models.CharField(max_length=20,null=True)
    payment_upi_id = models.CharField(max_length=20,null=True)
    total_amount = models.FloatField(null=True, blank=True,default=0.0)
    payment_received = models.FloatField(null=True, blank=True,default=0.0)
    balance = models.FloatField(null=True, blank=True,default=0.0)

class DeletedPaymentIn(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    rec_no = models.BigIntegerField(null=True)


class PaymentInTransactionHistory(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    payment = models.ForeignKey(PaymentIn,on_delete=models.CASCADE,null=True)
    
    CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
    ]
    action = models.CharField(max_length=20, choices=CHOICES,null=True)
    date = models.DateField(null=True,blank=True)

#------------------------------------end-------------------------------------------------

class DeliveryChallan(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE,null=True)
    challan_no = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    party_name = models.CharField(max_length=150)
    contact = models.CharField(max_length=255,null=True,blank=True)
    billing_address = models.TextField()
    state_of_supply = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    subtotal = models.FloatField(null=True, blank=True)
    igst = models.FloatField(null=True,blank=True)
    cgst = models.FloatField(null=True,blank=True)
    sgst = models.FloatField(null=True,blank=True)
    tax_amount =  models.FloatField(null=True,blank=True)
    adjustment = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    balance = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True)
    is_converted = models.BooleanField(null=True, default=False)
    
    
class DeliveryChallanItems(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    cid = models.ForeignKey(DeliveryChallan, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200)
    hsn = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(null=True, blank=True)
    tax = models.CharField(max_length=10)
    discount = models.FloatField(null=True, blank=True)
    total = models.FloatField()
    
    
class DeliveryChallanTransactionHistory(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    challan = models.ForeignKey(DeliveryChallan,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(auto_now_add=True,auto_now=False,null=True)
    action = models.CharField(max_length=255)
    
class ExpenseHistory(models.Model):
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    expense = models.ForeignKey(Expense,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(auto_now_add=True,auto_now=False,null=True)
    action = models.CharField(max_length=255) 
    
    
class LoanAccounts(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE,null=True,blank=True)
    account_name = models.TextField(max_length=255,null=True,blank=True)
    lender_bank = models.TextField(max_length=255,null=True,blank=True)
    account_number = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(max_length=255,null=True,blank=True)
    loan_amount = models.CharField(max_length=100,default='0',null=True,blank=True)
    proccessing_fee =models.DecimalField(max_digits=10, decimal_places=2, default=0.00,null=True,blank=True)
    date = models.DateField(null=True, blank=True)
    loan_received = models.CharField(max_length=255,null=True,blank=True)

    upi_id=models.CharField(max_length=255,null=True,default=0,blank=True)
    cheque_number= models.CharField(max_length=255,null=True,default=0,blank=True)
    
    interest_rate =models.DecimalField(max_digits=10, decimal_places=2, default=0.00,null=True,blank=True)
    duration =models.CharField(max_length=255,null=True,blank=True)
    lr = models.CharField(max_length=255,null=True,blank=True)

    upi_id_for_fee=models.CharField(max_length=255,null=True,default=0,blank=True)
    cheque_number_for_fee= models.CharField(max_length=255,null=True,default=0,blank=True)

    total_amount =models.CharField(max_length=100,default='0',null=True,blank=True)

class makepayment(models.Model):
    loan_account = models.ForeignKey(LoanAccounts, on_delete=models.CASCADE, null=True, blank=True)
    principal_amount = models.CharField(max_length=100, default='0', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    interest_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    total_amount = models.CharField(max_length=100, default='0', null=True, blank=True)
    loan_received = models.CharField(max_length=255, null=True, blank=True)

    upi_id=models.CharField(max_length=255,null=True,default=0,blank=True)
    cheque_number= models.CharField(max_length=255,null=True,default=0,blank=True)


class AdditionalLOan(models.Model):
    loan_account = models.ForeignKey(LoanAccounts, on_delete=models.CASCADE, null=True, blank=True)
    makepayment = models.ForeignKey(makepayment, on_delete=models.CASCADE, null=True, blank=True)
    additional_loan = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    interest_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    total_loan = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    loan_received = models.CharField(max_length=255, null=True, blank=True)
    upi_id=models.CharField(max_length=255,null=True,default=0,blank=True)
    cheque_number= models.CharField(max_length=255,null=True,default=0,blank=True)
 

class LoanHistory(models.Model):
    ADD = 'add'
    EDIT = 'edit'

    ACTION_CHOICES = [
        (ADD, 'Add'),
        (EDIT, 'Edit'),
    ]

    loan_account = models.ForeignKey(LoanAccounts, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=7, choices=ACTION_CHOICES, default=ADD) 
    
    
class CreditNote(models.Model):
    retrn_no=models.IntegerField(default=0,null=True,blank=True)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE,blank=True,null=True)
    partymob=models.CharField(null=True,blank=True,max_length=255)
    invoiceno=models.CharField(null=True,blank=True,max_length=255)
   
    supplyplace = models.CharField(max_length=100, default='')
   
    pay_method = models.CharField(max_length=255, default='', null=True)
    cheque_no = models.CharField(max_length=255, default='', null=True)
    upi_no = models.CharField(max_length=255, default='', null=True)
    bankaccount=models.CharField(max_length=255, default='', null=True)
    subtotal = models.IntegerField(default=0, null=True)
    igst = models.CharField(max_length=100,default=0, null=True)
    cgst = models.CharField(max_length=100,default=0, null=True)
    sgst = models.CharField(max_length=100,default=0, null=True)
    taxamount = models.CharField(max_length=100,default=0, null=True)
    adjust = models.CharField(max_length=100,default=0, null=True)
    grandtotal = models.FloatField(default=0, null=True)
    advance=models.CharField(null=True,blank=True,max_length=255)
    balance=models.CharField(null=True,blank=True,max_length=255)
    invoice_date=models.DateField()
    date=models.DateField(null=True,blank=True,max_length=255)
    description=models.CharField(null=True,blank=True,max_length=255)
    tot_credit_no = models.IntegerField(default=0, null=True)
    
    
class CreditNoteItem(models.Model):
    creditnote = models.ForeignKey(CreditNote,on_delete=models.CASCADE)
    company = models.ForeignKey(company,on_delete=models.CASCADE)
    product = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, null=True)
    rate=models.IntegerField(default=0, null=True)
    total = models.IntegerField(default=0, null=True)
    tax = models.CharField(max_length=100)
    discount = models.CharField(max_length=100,default=0, null=True)
    
class CreditNoteTransactionHistory(models.Model):
    creditnote = models.ForeignKey(CreditNote,on_delete=models.CASCADE)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
        ]
    action = models.CharField(max_length=20, choices=CHOICES)
    transactiondate = models.DateField(auto_now=True)
    
    
class BalanceAmount(models.Model):
    loan_account = models.ForeignKey(LoanAccounts, on_delete=models.CASCADE, null=True, blank=True)
    makepayment = models.ForeignKey(makepayment, on_delete=models.CASCADE, null=True, blank=True)
    additional_loan = models.ForeignKey(AdditionalLOan, on_delete=models.CASCADE, null=True, blank=True)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)