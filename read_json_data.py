import json

class JsonDataHandler:
    @staticmethod
    def parse_token_creation_log(log):
        try:
            # Parse the JSON log string
            data = json.loads(log)
            
            # Extract and format the key information
            parsed_data = {
                "Signature": data.get("signature"),
                "Mint Address": data.get("mint"),
                "Trader Public Key": data.get("traderPublicKey"),
                "Transaction Type": data.get("txType"),
                "Initial Buy": data.get("initialBuy"),
                "SOL Amount": data.get("solAmount"),
                "Bonding Curve Key": data.get("bondingCurveKey"),
                "vTokens in Bonding Curve": data.get("vTokensInBondingCurve"),
                "vSOL in Bonding Curve": data.get("vSolInBondingCurve"),
                "Market Cap (SOL)": data.get("marketCapSol"),
                "Token Name": data.get("name"),
                "Token Symbol": data.get("symbol"),
                "Token URI": data.get("uri"),
                "Pool": data.get("pool")
            }

            # Format the parsed data into a clean string for logging
            clean_output = "\n".join([f"{key}: {value}" for key, value in parsed_data.items() if value is not None])
            return clean_output
        except json.JSONDecodeError:
            return "Error: Invalid JSON data."
        except Exception as e:
            return f"Error parsing token creation log: {e}"


