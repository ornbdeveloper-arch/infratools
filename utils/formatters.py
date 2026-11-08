def format_bytes(size):
    if size >= 1024 ** 3:
        gib = size / (1024 ** 3)
        return f"{gib:.2f} GiB"
    elif size >= 1024 ** 2:
        mib = size /(1024 ** 2)
        return f"{mib:.2f} MiB"
    elif size >= 1024:
        kib = size / 1024
        return f"{kib:.2f} KiB"
    else:
        return f"{size:.2f} B" 
