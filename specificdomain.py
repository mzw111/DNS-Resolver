import sys
from collections import namedtuple

try:
    from dnsresolver import DNSResolver
except ImportError:
    print("Error: Could not import DNSResolver class")
    sys.exit(1)

def main():
    if len(sys.argv) > 1:
        domains = sys.argv[1:]
    else:
        # If no arguments, ask the user for input
        user_input = input("Enter the domain(s) to resolve, separated by spaces: ")
        # Split the input string into a list of domains
        domains = user_input.split()

    if not domains:
        print("No domains provided. Exiting.")
  
        sys.exit(0)
    
    resolver = DNSResolver()
    resolver.debug = True     
    
    try:
        print("DNS Resolution Results:")
        print("-" * 50)
        
        # Resolve each domain
        for domain in domains:
            print(f"\nResolving {domain}...")
            result = resolver.resolve(domain)
            
            if result:
                print(f"✓ Successfully resolved {domain}:")
                for domain_name, ttl, ip in result:
                    print(f"  - {domain_name} -> {ip} (TTL: {ttl}s)")
            else:
                print(f"✗ Failed to resolve {domain}")
    
    finally:
        # Clean up resources
        resolver.close()
        print("\nDNS resolver closed")

if __name__ == "__main__":
    main()