#Functions for cloud computing

aws_discount = 0.95
gg_discount = 1.0
mi_discount = 1.0

#=============== Storage: Amazon ===============================================
def aws_s3_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.023 * storage + 0.0007 * d_return + 0.002 * d_scan + 0.05 * write_ops + 0.004 * read_ops
    price *= aws_discount
    return price

def aws_s3ia_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.0125 * storage + 0.01 * d_return + 0.002 * d_scan + 0.1 * write_ops + 0.01 * read_ops
    price *= aws_discount
    return price

def aws_glacier_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.004 * storage + 0.0025 * d_return + 0.001 * d_scan + 0.5 * write_ops + 0.25 * read_ops
    price *= aws_discount
    return price

#=============== Storage: Google ===============================================
def google_mr_price(storage, d_return, d_scan, write_ops, read_ops):
    price =  0.026 * storage + 0.00 * d_return + 0.00 * d_scan + 0.05 * write_ops + 0.05 * read_ops
    price *= gg_discount
    return price

def google_near_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.01 * storage + 0.01 * d_return + 0.00 * d_scan + 0.1 * write_ops + 0.1 * read_ops
    price *= gg_discount
    return price

def google_cold_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.007 * storage + 0.05 * d_return + 0.00 * d_scan + 0.1 * write_ops + 0.1 * read_ops
    price *= gg_discount
    return price

#=============== Storage: MiStorage ============================================
def mi_base_price(storage, d_return, d_scan, write_ops, read_ops):
    price =  0.0075 * storage + 0.00 * d_return + 0.00 * d_scan + 0.00 * write_ops + 0.00 * read_ops
    price *= mi_discount
    return price

def mi_bs_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.009375 * storage + 0.00 * d_return + 0.00 * d_scan + 0.00 * write_ops + 0.00 * read_ops
    price *= mi_discount
    return price

def mi_br_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.015 * storage + 0.00 * d_return + 0.00 * d_scan + 0.00 * write_ops + 0.00 * read_ops
    price *= mi_discount
    return price

def mi_sr_price(storage, d_return, d_scan, write_ops, read_ops):
    price = 0.01875 * storage + 0.00 * d_return + 0.00 * d_scan + 0.00 * write_ops + 0.00 * read_ops
    price *= mi_discount
    return price
