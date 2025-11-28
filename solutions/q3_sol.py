def generate_monthly_report(transactions):
    monthly_report = {}
    
    for transaction in transactions:
        year, month, day = transaction['timestamp'].split('-')
        month_key = f"{year}-{month}"
        
        if month_key not in monthly_report:
            monthly_report[month_key] = {'total_credit': 0, 'total_debit': 0, 'net_balance': 0}
        else:
            # Update totals for the current month
            if transaction['type'] == 'credit':
                monthly_report[month_key]['total_credit'] += transaction['amount']
            elif transaction['type'] == 'debit':
                monthly_report[month_key]['total_debit'] += transaction['amount']
            
            # Update net balance
            monthly_report[month_key]['net_balance'] = (
                monthly_report[month_key]['total_credit'] - monthly_report[month_key]['total_debit']
            )
    
    return monthly_report

