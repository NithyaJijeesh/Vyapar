from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register', views.register, name='register'),
    
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('sale_invoices', views.sale_invoices, name='sale_invoices'),
    path('estimate_quotation', views.estimate_quotation, name='estimate_quotation'),
    path('payment_in', views.payment_in, name='payment_in'),
    # path('sale_order', views.sale_order, name='sale_order'),
    path('delivery_challan', views.delivery_challan, name='delivery_challan'),
    path('sale_return_cr', views.sale_return_cr, name='sale_return_cr'),

    # created by athul
    # path('settings', views.settings, name='settings'),
    path('hide_options', views.hide_options, name='hide_options'),

    path('staffhome', views.staffhome, name='staffhome'),
    path('adminhome', views.adminhome, name='adminhome'),
    
    
    path('staff_register', views.staff_register, name='staff_register'),
    path('staff_registraction', views.staff_registraction, name='staff_registraction'),
    path('company_reg', views.company_reg, name='company_reg'),
    path('company_reg2', views.company_reg2, name='company_reg2'),
    path('add_company', views.add_company, name='add_company'),
    path('log_page', views.log_page, name='log_page'),
    path('login', views.login, name='login'),
    path('adminaccept/<id>', views.adminaccept, name='adminaccept'),
    path('adminreject/<id>', views.adminreject, name='adminreject'),
    path('View_staff', views.View_staff, name='View_staff'),
    path('companyaccept/<id>', views.companyaccept, name='companyaccept'),
    path('companyreject/<id>', views.companyreject, name='companyreject'),
    path('client_request', views.client_request, name='client_request'),
    path('client_details', views.client_details, name='client_details'),
    path('staff_request', views.staff_request, name='staff_request'),
    path('payment_term', views.payment_term, name='payment_term'),
    path('add_payment_terms', views.add_payment_terms, name='add_payment_terms'),
    path('Allmodule/<uid>', views.Allmodule, name='Allmodule'),
    path('addmodules/<uid>', views.addmodules, name='addmodules'),
    path('client_request_overview/<id>', views.client_request_overview, name='client_request_overview'),
    path('client_details_overview/<id>', views.client_details_overview, name='client_details_overview'),


    
    path('companyreport', views.companyreport, name='companyreport'),
    path('Companyprofile', views.Companyprofile, name='Companyprofile'),
    path('editcompanyprofile', views.editcompanyprofile, name='editcompanyprofile'),
    path('editcompanyprofile_action', views.editcompanyprofile_action, name='editcompanyprofile_action'),
    path('editmodule', views.editmodule, name='editmodule'),
    path('editmodule_action', views.editmodule_action, name='editmodule_action'),
    path('admin_notification', views.admin_notification, name='admin_notification'),
    path('module_updation_details/<mid>', views.module_updation_details, name='module_updation_details'),
    path('module_updation_ok/<mid>', views.module_updation_ok, name='module_updation_ok'),
    path('staff_profile', views.staff_profile, name='staff_profile'),
    path('editstaff_profile', views.editstaff_profile, name='editstaff_profile'),
    path('editstaff_profile_action', views.editstaff_profile_action, name='editstaff_profile_action'),

    path('distributor_home', views.distributor_home, name='distributor_home'),
    path('distributor_reg', views.distributor_reg, name='distributor_reg'),
    path('distributor_reg_action', views.distributor_reg_action, name='distributor_reg_action'),
    path('distributors', views.distributors, name='distributors'),
    path('clients', views.clients, name='clients'),
    path('distributor_request', views.distributor_request, name='distributor_request'),
    path('admin_distributor_accept/<id>', views.admin_distributor_accept, name='admin_distributor_accept'),
    path('admin_distributor_reject/<id>', views.admin_distributor_reject, name='admin_distributor_reject'),
    path('distributor_request_overview/<id>', views.distributor_request_overview, name='distributor_request_overview'),
    path('distributor_details', views.distributor_details, name='distributor_details'),
    path('distributor_details_overview/<id>', views.distributor_details_overview, name='distributor_details_overview'),
    path('dcompany_request', views.dcompany_request, name='dcompany_request'),
    path('dcompany_details', views.dcompany_details, name='dcompany_details'),
    path('dcompany_request_overview/<id>', views.dcompany_request_overview, name='dcompany_request_overview'),
    path('distributor_accept_company/<id>', views.distributor_accept_company, name='distributor_accept_company'),
    path('distributor_reject_company/<id>', views.distributor_reject_company, name='distributor_reject_company'),
    path('dcompany_details_overview/<id>', views.dcompany_details_overview, name='dcompany_details_overview'),
    path('distributor_profile', views.distributor_profile, name='distributor_profile'),
    
    # ========================================   ASHIKH V U (START) ======================================================

    path('item_create', views.item_create, name='item_create'),
    path('items_list/<int:pk>', views.items_list, name='items_list'),
    path('item_create_new', views.item_create_new, name='item_create_new'),
    path('item_delete/<int:pk>', views.item_delete, name='item_delete'),
    path('item_view_or_edit/<int:pk>', views.item_view_or_edit, name='item_view_or_edit'),
    path('item_unit_create', views.item_unit_create, name='item_unit_create'),
    path('item_update/<int:pk>', views.item_update, name='item_update'),
    path('item_search_filter', views.item_search_filter, name='item_search_filter'),
    path('item_get_detail/<int:pk>', views.item_get_detail, name='item_get_detail'),
    path('item_get_details_for_modal_target/<int:pk>', views.item_get_details_for_modal_target, name='item_get_details_for_modal_target'),
    path('ajust_quantity/<int:pk>', views.ajust_quantity, name='ajust_quantity'),
    path('transaction_delete/<int:pk>', views.transaction_delete, name='transaction_delete'),
    path('item_transaction_view_or_edit/<int:pk>/<int:tran>', views.item_transaction_view_or_edit, name='item_transaction_view_or_edit'),
    path('update_adjusted_transaction/<int:pk>/<int:tran>', views.update_adjusted_transaction, name='update_adjusted_transaction'),
    path('item_delete_open_stk/<int:pk>',views.item_delete_open_stk,name='item_delete_open_stk'),
    path('item_histories/<int:id>', views.item_histories, name='item_histories'),

    path('bank_create',views.bank_create,name='bank_create'),
    path('banks_list/<int:pk>',views.banks_list,name='banks_list'),
    path('get_bank_to_bank',views.get_bank_to_bank,name='get_bank_to_bank'),
    path('get_bank_to_cash',views.get_bank_to_cash,name='get_bank_to_cash'),
    path('get_cash_to_bank',views.get_cash_to_bank,name='get_cash_to_bank'),
    path('get_adjust_bank_balance',views.get_adjust_bank_balance,name='get_adjust_bank_balance'),
    path('bank_create_new',views.bank_create_new,name='bank_create_new'),
    path('bank_delete/<int:pk>',views.bank_delete,name='bank_delete'),
    path('account_num_check',views.account_num_check,name='account_num_check'),
    path('account_num_check_for_edit/<int:pk>',views.account_num_check_for_edit,name='account_num_check_for_edit'),
    path('bank_ifsc_check',views.bank_ifsc_check,name='bank_ifsc_check'),
    path('bank_view_or_edit/<int:pk>',views.bank_view_or_edit,name='bank_view_or_edit'),
    path('bank_update/<int:pk>',views.bank_update,name='bank_update'),
    path('bank_to_bank_transaction_create',views.bank_to_bank_transaction_create,name='bank_to_bank_transaction_create'),
    path('bank_to_cash_transaction_create',views.bank_to_cash_transaction_create,name='bank_to_cash_transaction_create'),
    path('cash_to_bank_transaction_create',views.cash_to_bank_transaction_create,name='cash_to_bank_transaction_create'),
    path('get_adjust_bank_balance_create',views.get_adjust_bank_balance_create,name='get_adjust_bank_balance_create'),
    path('delete_bank_open_balance/<int:pk>',views.delete_bank_open_balance,name='delete_bank_open_balance'),
    path('delete_bank_transaction/<int:pk>/<int:bank_id>',views.delete_bank_transaction,name='delete_bank_transaction'),
    path('view_or_edit_bank_transaction/<int:pk>/<int:bank_id>',views.view_or_edit_bank_transaction,name='view_or_edit_bank_transaction'),
    path('update_bank_transaction/<int:pk>/<int:bank_id>',views.update_bank_transaction,name='update_bank_transaction'),
    path('import_from_excel/<int:pk>',views.import_from_excel,name='import_from_excel'),
    path('import_statement_from_excel/<int:pk>',views.import_statement_from_excel,name='import_statement_from_excel'),
    path('transaction_history/<int:pk>/<int:bank_id>',views.transaction_history,name='transaction_history'),
    path('bank_transaction_statement/<int:bank_id>',views.bank_transaction_statement,name='bank_transaction_statement'),
    
    # ========================================   ASHIKH V U (END) ======================================================
    
    #______________Parties(new)_________________Antony Tom___________________________

    path('add_parties', views.add_parties, name='add_parties'),
    path('save_parties', views.save_parties, name='save_parties'),
    path('view_parties/<int:pk>', views.view_parties, name='view_parties'),
    path('view_party/<int:id>', views.view_party, name='view_party'),
    path('edit_party/<int:id>', views.edit_party, name='edit_party'),
    path('edit_saveparty/<int:id>', views.edit_saveparty, name='edit_saveparty'),
    path('deleteparty/<int:id>', views.deleteparty, name='deleteparty'),
    path('party_histories/<int:id>', views.party_histories, name='party_histories'),
    path('import_parties', views.import_parties, name='import_parties'),
    path('downloadPartySampleImportFile', views.downloadPartySampleImportFile, name='downloadPartySampleImportFile'),

    #End
    path('view_purchasebill',views.view_purchasebill,name='view_purchasebill'),
    path('add_purchasebill',views.add_purchasebill,name='add_purchasebill'), 
    path('create_purchasebill',views.create_purchasebill,name='create_purchasebill'),
    path('edit_purchasebill/<int:id>',views.edit_purchasebill,name='edit_purchasebill'),
    path('update_purchasebill/<int:id>',views.update_purchasebill,name='update_purchasebill'),
    path('details_purchasebill/<int:id>',views.details_purchasebill,name='details_purchasebill'),
    path('history_purchasebill/<int:id>',views.history_purchasebill,name='history_purchasebill'),
    path('delete_purchasebill/<int:id>',views.delete_purchasebill,name='delete_purchasebill'), 
    path('import_purchase_bill',views.import_purchase_bill,name='import_purchase_bill'), 
    path('billhistory',views.billhistory,name='billhistory'), 
    path('bankdata',views.bankdata,name='bankdata'), 
    path('savecustomer',views.savecustomer,name='savecustomer'),
    path('cust_dropdown',views.cust_dropdown,name='cust_dropdown'),
    path('saveitem',views.saveitem,name='saveitem'),
    path('item_dropdown',views.item_dropdown,name='item_dropdown'),
    path('custdata',views.custdata,name='custdata'),
    path('itemdetails',views.itemdetails,name='itemdetails'),
    path('add_purchaseorder',views.add_purchaseorder,name='add_purchaseorder'),
    path('view_purchaseorder',views.view_purchaseorder,name='view_purchaseorder'),
    
    # =========== estimate & delivery challan=========== shemeem - start =======================================
    path('create_estimate',views.create_estimate, name='create_estimate'),
    path('add_new_party',views.addNewParty, name='addNewParty'),
    path('add_new_item',views.addNewItem, name='addNewItem'),
    path('get_party_details',views.getPartyDetails, name='getPartyDetails'),
    path('get_item_data',views.getItemData, name='getItemData'),
    path('create_new_estimate',views.createNewEstimate, name='createNewEstimate'),
    path('get_party_list',views.getPartyList, name= 'getPartyList'),
    path('get_item_list',views.getItemList, name = 'getItemList'),
    path('estimate_filter_with_date',views.estimateFilterWithDate, name='estimateFilterWithDate'),
    path('estimate_filter_with_ref',views.estimateFilterWithRef, name='estimateFilterWithRef'),
    path('estimate_filter_with_name',views.estimateFilterWithName, name='estimateFilterWithName'),
    path('estimate_filter_with_total',views.estimateFilterWithTotal, name='estimateFilterWithTotal'),
    path('estimate_filter_with_bal',views.estimateFilterWithBal, name='estimateFilterWithBal'),
    path('estimate_filter_with_stat',views.estimateFilterWithStat, name='estimateFilterWithStat'),
    path('estimate_in_between', views.estimateInBetween, name='estimateInBetween'),
    path('edit_estimate/<int:id>',views.editEstimate, name='editEstimate'),
    path('update_estimate/<int:id>',views.updateEstimate, name= 'updateEstimate'),
    path('delete_estimate_quotation/<int:id>',views.deleteEstimate, name = 'deleteEstimate'),
    path('estimate_transaction_history/<int:id>',views.estimateTransactionHistory, name='estimateTransactionHistory'),
    path('import_estimate_form_excel',views.importEstimateFromExcel, name='importEstimateFromExcel'),
    path('download_estimate_sample_file',views.downloadEstimateSampleImportFile, name = 'downloadEstimateSampleImportFile'),
    path('estimate_bill_pdf_view/<int:id>',views.estimateBillPdf, name='estimateBillPdf'),
    path('view_estimate_bill/<int:id>',views.viewEstimate, name='viewEstimate'),


    path('create_delivery_challan',views.createDeliveryChallan, name='createDeliveryChallan'),
    path('create_new_delivery_challan',views.createNewDeliveryChallan, name='createNewDeliveryChallan'),
    path('challan_in_between', views.challanInBetween, name='challanInBetween'),
    path('challan_filter_with_date',views.challanFilterWithDate, name='challanFilterWithDate'),
    path('challan_filter_with_duedate',views.challanFilterWithDueDate, name='challanFilterWithDueDate'),
    path('challan_filter_with_challan_no',views.challanFilterWithChallanNo, name='challanFilterWithChallanNo'),
    path('challan_filter_with_name',views.challanFilterWithName, name='challanFilterWithName'),
    path('challan_filter_with_total',views.challanFilterWithTotal, name='challanFilterWithTotal'),
    path('challan_filter_with_bal',views.challanFilterWithBal, name='challanFilterWithBal'),
    path('challan_filter_with_stat',views.challanFilterWithStat, name='challanFilterWithStat'),
    path('delete_delivery_challan/<int:id>',views.deleteChallan, name = 'deleteChallan'),
    path('edit_challan/<int:id>',views.editChallan, name='editChallan'),
    path('update_challan/<int:id>',views.updateChallan, name= 'updateChallan'),
    path('challan_transaction_history/<int:id>',views.challanTransactionHistory, name='challanTransactionHistory'),
    path('import_challan_form_excel',views.importChallanFromExcel, name='importChallanFromExcel'),
    path('download_challan_sample_file',views.downloadChallanSampleImportFile, name = 'downloadChallanSampleImportFile'),
    path('challan_bill_pdf_view/<int:id>',views.challanBillPdf, name='challanBillPdf'),
    path('view_challan_bill/<int:id>',views.viewChallan, name='viewChallan'),
    # ===================================== shemeem - end ==================================================
    
    #______________Sales Invoice_________________Antony Tom___________________________
    path('itemdetailinvoice', views.itemdetailinvoice, name='itemdetailinvoice'),
    path('add_salesinvoice', views.add_salesinvoice, name='add_salesinvoice'),
    path('save_sales_invoice', views.save_sales_invoice, name='save_sales_invoice'),
    path('itemdata_salesinvoice',views.itemdata_salesinvoice,name='itemdata_salesinvoice'),
    path('itemdata_salesinvoiceedit',views.itemdata_salesinvoiceedit,name='itemdata_salesinvoiceedit'),
    path('view_salesinvoice',views.view_salesinvoice,name='view_salesinvoice'),
    path('api/bank-details/<str:bank_name>/',views.get_bank_details, name='get_bank_details'),
    path('get_total_balance/', views.get_total_balance, name='get_total_balance'),
    path('edit_salesinvoice/<int:id>/', views.edit_salesinvoice, name='edit_salesinvoice'),
    path('editsave_salesinvoice/<int:id>/', views.editsave_salesinvoice, name='editsave_salesinvoice'),
    path('salesinvoice_save_parties', views.salesinvoice_save_parties, name='salesinvoice_save_parties'),
    path('deletesalesinvoice/<int:id>/', views.deletesalesinvoice, name='deletesalesinvoice'),
    path('graph_salesinvoice', views.graph_salesinvoice, name='graph_salesinvoice'),
    path('salesinvoicehistory/<int:id>/', views.salesinvoicehistory, name='salesinvoicehistory'),
    path('salesinvoice_billtemplate/<int:id>/', views.salesinvoice_billtemplate, name='salesinvoice_billtemplate'),
    path('importsalesinvoice_excel', views.importsalesinvoice_excel, name='importsalesinvoice_excel'),
    path('api/profit_loss_data/<int:year>/', views.profit_loss_data, name='profit_loss_data_year'),
    path('api/party-details/<str:party_name>/',views.party_details, name='party_details'),
    #End
    
    # ========================================   Haripriya B Nair (start) ======================================================
    path('view_purchasedebit',views.view_purchasedebit,name='view_purchasedebit'),
    path('add_debitnote',views.add_debitnote,name='add_debitnote'),
    path('custdata1',views.custdata1,name='custdata1'),
    path('cust_dropdown1',views.cust_dropdown1,name='cust_dropdown1'),
    path('savecustomer1',views.savecustomer1,name='savecustomer1'),
    path('saveitem1',views.saveitem1,name='saveitem1'),
    path('item_dropdowns',views.item_dropdowns,name='item_dropdowns'),
    path('itemdetail',views.itemdetail,name='itemdetail'),
    path('create_debitnotes',views.create_debitnotes,name='create_debitnotes'),
    path('purchasebilldata',views.purchasebilldata,name='purchasebilldata'),
    
    path('bankdata1',views.bankdata1,name='bankdata1'),
    path('delete_debit/<int:id>',views.delete_debit,name='delete_debit'),
    path('edit_debitnote/<int:id>',views.edit_debitnote,name='edit_debitnote'),
    path('update_debitnote/<int:id>',views.update_debitnote,name='update_debitnote'),
    path('history_debitnote/<int:id>',views.history_debitnote,name='history_debitnote'),
    path('debthistory',views.debthistory,name='debthistory'),
    path('import_debitnote',views.import_debitnote,name='import_debitnote'),
    path('details_debitnote/<int:id>',views.details_debitnote,name='details_debitnote'),

# ========================================   Haripriya B Nair (end) =============

    path('sharedebitToEmail/<int:id>',views.sharedebitToEmail,name='sharedebitToEmail'),
    
    path('distributor_notification',views.distributor_notification,name='distributor_notification'),
    path('distributor_module_updation/<int:mid>',views.distributor_module_updation,name='distributor_module_updation'),
    path('distributor_module_updation_ok/<int:mid>',views.distributor_module_updation_ok,name='distributor_module_updation_ok'),
    path('expense',views.expense,name='expense'),
    path('newexpenses',views.newexpenses,name='newexpenses'),
    path('partydata',views.partydata,name='partydata'),
    path('add_party_in_expense',views.add_party_in_expense,name='add_party_in_expense'),
    path('create_expense_category',views.create_expense_category,name='create_expense_category'),
    path('create_expense',views.create_expense,name='create_expense'),
    path('view_expense/<int:eid>',views.view_expense,name='view_expense'),
    path('expense_details/<int:eid>',views.expense_details,name='expense_details'),
    path('edit_expense/<int:eid>',views.edit_expense,name='edit_expense'),
    path('edit_expense_action/<int:eid>',views.edit_expense_action,name='edit_expense_action'),
    path('delete_expense/<int:eid>',views.delete_expense,name='delete_expense'),
    path('view_expense/import_expense',views.import_expense,name='import_expense'),
    
    path('create_purchaseorder',views.create_purchaseorder,name='create_purchaseorder'),
    path('edit_purchaseorder/<int:id>',views.edit_purchaseorder,name='edit_purchaseorder'),
    path('update_purchaseorder/<int:id>',views.update_purchaseorder,name='update_purchaseorder'),
    path('details_purchaseorder/<int:id>',views.details_purchaseorder,name='details_purchaseorder'),
    path('delete_purchaseorder/<int:id>',views.delete_purchaseorder,name='delete_purchaseorder'),
    path('orderhistory',views.orderhistory,name='orderhistory'), 
    path('convert_to_bill/<int:id>',views.convert_to_bill,name='convert_to_bill'),
    path('import_purchase_order',views.import_purchase_order,name='import_purchase_order'),  
    path('history_purchaseorder/<int:id>',views.history_purchaseorder,name='history_purchaseorder'), 
    
    #Nsaneen
    path('sale_order', views.sale_order, name='sale_order'),
    path('saleorder_create', views.saleorder_create, name='saleorder_create'),
    path('getparty', views.getparty, name='getparty'),
    path('getproduct', views.getproduct, name='getproduct'),
    path('getacc', views.getacc, name='getacc'),
    path('create_saleorder', views.create_saleorder, name='create_saleorder'),
    path('saleorder_view/<int:id>', views.saleorder_view, name='saleorder_view'),
    path('delete_saleorder/<int:id>', views.delete_saleorder, name='delete_saleorder'),
    path('import_excel', views.import_excel, name='import_excel'),
    path('add_party', views.add_party, name='add_party'),
    path('add_item', views.add_item, name='add_item'),
    path('sales_transaction/<int:id>', views.sales_transaction, name='sales_transaction'),
    path('saleorder_edit/<int:id>', views.saleorder_edit, name='saleorder_edit'),
    path('edit_saleorder/<int:id>', views.edit_saleorder, name='edit_saleorder'),
    path('saleorderto_invoice/<int:id>', views.saleorderto_invoice, name='saleorderto_invoice'),
    path('saleorder_convert/<int:sid>', views.saleorder_convert, name='saleorder_convert'),
    #End
    
    path('get_bill_date',views.get_bill_date,name='get_bill_date'),
    
    #salesinvoiceurl(new)
    path('item_save_invoice', views.item_save_invoice, name='item_save_invoice'),
    path('item_invoicedropdown', views.item_invoicedropdown, name='item_invoicedropdown'),
    #End
    
    path('expense_cat_dropdown',views.expense_cat_dropdown,name='expense_cat_dropdown'),
    
    # =========== payment out=========== Anuvinda - start =======================================
     path('view_paymentout',views.view_paymentout,name='view_paymentout'),
     path('add_paymentout',views.add_paymentout,name='add_paymentout'),
     path('create_paymentout',views.create_paymentout,name='create_paymentout'),
     path('delete_paymentout/',views.delete_paymentout,name='delete_paymentout'), 
     path('details_paymentout/<int:id>/', views.details_paymentout, name='details_paymentout'),
     path('edit_paymentout/<int:id>/',views.edit_paymentout, name='edit_paymentout'),
     path('add_pay/',views.add_pay, name='add_pay'),
     path('create_addpaymentout',views.create_addpaymentout,name='create_addpaymentout'), 
     path('update_paymentout/<int:id>/', views.update_paymentout, name='update_paymentout'),
     path('paymentout_history/<int:id>/',views.paymentout_history, name='paymentout_history'),
     path('send-email/',views.send_email, name='send_email'),
     path('get_party_details/', views.get_party_details, name='get_party_details'),
     #End
     
     # =====================================gstr-3B gstr9 AKSHAYA ===============================================================
    
    path('gstr3b',views.gstr3b, name='gstr3b'),
    path('sharegstr3BToEmail',views.sharegstr3BToEmail, name='sharegstr3BToEmail'),
    path('gstr9',views.gstr9, name='gstr9'),
    path('sharegstr9ToEmail',views.sharegstr9ToEmail, name='sharegstr9ToEmail'),
    #End
    
    #______________Payment In__________________shemeem________________________________
    path('listout_paymentin',views.paymentIn, name='paymentIn'),
    path('create_payment_in',views.createPaymentIn,name='createPaymentIn'),
    path('get_bank_acc_number',views.getBankDetails, name='getBankDetails'),
    path('create_new_payment_in',views.createNewPaymentIn, name='createNewPaymentIn'),
    path('delete_payment_in/<int:id>',views.deletePaymentIn, name='deletePaymentIn'),
    path('payment_trans_history',views.paymentHistory, name = 'paymentHistory'),
    path('view_payment_in/<int:id>',views.viewPaymentIn, name='viewPaymentIn'),
    path('share_paymentin_to_email/<int:id>',views.sharePaymentInToEmail,name='sharePaymentInToEmail'),
    path('edit_payment_in_receipt/<int:id>',views.editPaymentIn, name='editPaymentIn'),
    path('update_payment_in/<int:id>',views.updatePaymentIn, name='updatePaymentIn'),
    path('history_payment_in/<int:id>',views.paymentInHistory,name='paymentInHistory'),
    path('download_payment_sample_file',views.downloadPaymentSampleImportFile, name = 'downloadPaymentSampleImportFile'),
    path('import_payment_form_excel',views.importPaymentFromExcel, name='importPaymentFromExcel'),
    
    #Delivery challan and Estimate urls...
    path('convert_estimate_to_sales_order/<int:id>',views.convertEstimateToSalesOrder, name='convertEstimateToSalesOrder'),
    path('save_estimate_to_sales_order/<int:id>',views.saveEstimateToSalesOrder, name='saveEstimateToSalesOrder'),
    path('convert_estimate_to_invoice/<int:id>',views.convertEstimateToInvoice, name='convertEstimateToInvoice'),
    path('save_estimate_to_invoice/<int:id>',views.saveEstimateToInvoice, name='saveEstimateToInvoice'),
    path('convert_challan_to_invoice/<int:id>',views.convertChallanToInvoice, name='convertChallanToInvoice'),
    path('save_challan_to_invoice/<int:id>',views.saveChallanToInvoice, name='saveChallanToInvoice'),

    #_________________________________________________________________________________
    
    path('gstrr2',views.gstrr2,name='gstrr2'),
    path('gstrnew1',views.gstrnew1,name='gstrnew1'),
    path('sharepurchaseBillToEmail',views.sharepurchaseBillToEmail,name='sharepurchaseBillToEmail'),
    path('shareGSTR2purchaseBillToEmail',views.shareGSTR2purchaseBillToEmail,name='shareGSTR2purchaseBillToEmail'),
    
    path('shareinvoiceToEmail/<int:id>/', views.shareinvoiceToEmail, name='shareinvoiceToEmail'),
    path('order_to_bill/<int:id>',views.order_to_bill,name='order_to_bill'),
    
    path('sales_report',views.sales_report,name='sales_report'),
    path('purchase_report',views.purchase_report,name='purchase_report'),
    path('send_sale_report_via_mail',views.send_sale_report_via_mail,name='send_sale_report_via_mail'),
    path('send_purchase_report_via_mail',views.send_purchase_report_via_mail,name='send_purchase_report_via_mail'),
    path('day_book_report',views.day_book_report,name='day_book_report'),
    
    path('loan_accounts',views.loan_accounts,name='loan_accounts'),

    path('add_loan_accounts',views.add_loan_accounts,name='add_loan_accounts'),
    path('add_loan_accounts_function',views.add_loan_accounts_function,name='add_loan_accounts_function'),
    path('edit_loan_page/<int:eid>',views.edit_loan_page,name='edit_loan_page'),
    path('make_payment/<int:eid>',views.make_payment,name='make_payment'),

    path('edit_loan_page_function/<int:eid>',views.edit_loan_page_function,name='edit_loan_page_function'),

    path('loan_accounts_view_page/<int:eid>',views.loan_accounts_view_page,name='loan_accounts_view_page'),

    path('import-loan-accounts/', views.import_loan_accounts, name='import_loan_accounts'),
    
    path('ShareLoanStatementMail/<int:eid>', views.ShareLoanStatementMail, name='ShareLoanStatementMail'),
 

    path('additional_loan',views.additional_loan,name='additional_loan'),

    path('loan_account_history/<int:id>/',views.loan_account_history,name='loan_account_history'),

    
    path('LoanAccountDelete/<int:id>', views.LoanAccountDelete, name='LoanAccountDelete'),
    
    path('create_sale', views.create_sale, name='create_sale'),
    path('new_creditnote_item', views.new_creditnote_item, name='new_creditnote_item'),
    path('get_hsn_for_item',views.get_hsn_for_item,name='get_hsn_for_item'),
    path('get_party_number',views.get_party_number,name='get_party_number'),
   
    path('creditnote_list',views.creditnote_list,name='creditnote_list'),
    path('party_dropdown',views.party_dropdown,name='party_dropdown'),
    path('saveparty',views.saveparty,name='saveparty'),
    path('credit_bankdetails',views.credit_bankdetails,name='credit_bankdetails'),
    path('add_creditnote',views.add_creditnote,name='add_creditnote'),
    path('detail_creditnote/<int:id>/',views.detail_creditnote,name='detail_creditnote'),
   
    path('import_creditnote',views.import_creditnote,name='import_creditnote'),
    path('delete_CreditNote/<int:id>/', views.delete_CreditNote, name='delete_CreditNote'),
    path('creditnote_item_unit',views.creditnote_item_unit,name='creditnote_item_unit'),
    path('edit_creditnote/<int:id>/',views.edit_creditnote,name='edit_creditnote'),
    path('salesinvoicedata',views.salesinvoicedata,name='salesinvoicedata'),
    path('get_inv_date',views.get_inv_date,name='get_inv_date'),
    path('update_creditnote/<int:id>/',views.update_creditnote,name='update_creditnote'),
    path('history_creditnote/<int:id>',views.history_creditnote,name='history_creditnote'),
    path('credititemdetails',views.credititemdetails,name='credititemdetails'),
    
    path('additional_loan_function/<int:eid>', views.additional_loan_function, name='additional_loan_function'),
    
    path('email_saleorder/<int:id>', views.email_saleorder, name='email_saleorder'),
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)