import ip_address as ip

quad_doted_address = "16.8.4.1"
decimal_address = 268960769
binary_address = "00010000000010000000010000000001"

if ip.quad_doted_to_decimal(quad_doted_address) == decimal_address:
    print("quad-doted->decimal OK")
else:
    print("quad-doted->decimal FAILED")

if ip.decimal_to_quad_doted(decimal_address) == quad_doted_address:
    print("decimal->quad-doted OK")
else:
    print("decimal->quad-doted FAILED")

if ip.binary_to_decimal(binary_address) == decimal_address:
    print("binary->decimal OK")
else:
    print("binary->decimal FAILED")

if ip.decimal_to_binary(decimal_address) == binary_address:
    print("decimal->binary OK")
else:
    print("decimal->binary FAILED")

if ip.binary_to_quad_doted(binary_address) == quad_doted_address:
    print("binary->quad-doted OK")
else:
    print("binary->quad-doted FAILED")

if ip.quad_doted_to_binary(quad_doted_address) == binary_address:
    print("quad-doted->binary OK")
else:
    print("quad-doted->binary FAILED")
