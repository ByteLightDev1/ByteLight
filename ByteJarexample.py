from ByteLightProject import ByteJar

client = ByteJar()

client.start()

set_response = client.send_command("--set mycookie value mypassword")
print(set_response)

get_response = client.send_command("--get mycookie mypassword")
print(get_response)

delete_response = client.send_command("--del mycookie mypassword")
print(delete_response)

allget_response = client.send_command("--allget")
print(allget_response)

client.stop()
