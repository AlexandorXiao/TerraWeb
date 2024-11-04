from conf.main_config import CLOUDFLARE_IP_RANGES

class CloudflareHandler:
    def __init__(self, ip_ranges):
        self.ip_ranges = ip_ranges

    def is_cloudflare_ip(self, ip):
        for cf_ip_range in self.ip_ranges:
            if self.ip_in_range(ip, cf_ip_range):
                return True
        return False

    def ip_in_range(self, ip, ip_range):
        if '/' not in ip_range:
            ip_range += '/32'

        range_ip, netmask = ip_range.split('/')
        range_decimal = self.ip_to_decimal(range_ip)
        ip_decimal = self.ip_to_decimal(ip)
        wildcard_decimal = (2 ** (32 - int(netmask))) - 1
        netmask_decimal = ~wildcard_decimal
        return (ip_decimal & netmask_decimal) == (range_decimal & netmask_decimal)

    @staticmethod
    def ip_to_decimal(ip):
        parts = [int(part) for part in ip.split('.')]
        return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

    def get_real_ip(self, request):
        ip = request.headers.get('CF-Connecting-IP')
        if ip and self.is_cloudflare_ip(ip):
            return ip
        else:
            return request.remote_addr

cf_handler = CloudflareHandler(CLOUDFLARE_IP_RANGES)