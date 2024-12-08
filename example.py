from randomcontent import generate_number, generate_text, generate_structured_data,generate_identifier, format_data


# # Generate a random integer between 1 and 10
# print(generate_number(type="int", min=1, max=10))

# # Generate a random float between 0 and 1
# print(generate_number(type="float", min=0, max=1))

# # Generate a random number from a Gaussian distribution with mean 0 and std_dev 1
# print(generate_number(type="gaussian", mean=0, std_dev=1))

# # Generate a random choice from a list of options
# print(generate_number(type="choice", options=[10, 20, 30, 40]))

# # Generate a random number in the range of 0 to 100 with a step of 5
# print(generate_number(type="range", min=0, max=100, step=7))

# # Generate a random probability between 0 and 1
# print(generate_number(type="probability"))


#######################################################

# print(generate_text(type="sentence", length=12))  # Generates a sentence
# print(generate_text(type="poem", num_lines=4))    # Generates a poem


########################################################

# print(generate_identifier(type="uuid"))  # Generates a UUID-like string (32 characters)
# print(generate_identifier(type="credit_card"))  # Generates a credit card number (16 digits)
# print(generate_identifier(type="email"))  # Generates an email address
# print(generate_identifier(type="phone_number"))  # Generates a phone number
# print(generate_identifier(type="user_id", length=10))  # Generates a 10-character user ID

#################################################################

# Example schemas
schema_1 = {
    "name": "random_name",
    "email": "random_email",
    "age": "random_int(min=18, max=60)"
}

schema_2 = {
    "product_id": "random_int(min=1000, max=9999)",
    "price": "random_float(min=10.0, max=500.0)",
    "rating": "random_float(min=1.0, max=5.0)"
}

# Step 1: Generate structured data
mock_data = generate_structured_data(schema_1, count=5)

# Step 2: Format and save the data
format_data(mock_data, format_type="json", file_name="data")
format_data(mock_data, format_type="csv", file_name="data")
format_data(mock_data, format_type="parquet", file_name="data")

