from web3 import Web3


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/922ed38024ab46e3bb7e73785e8bcd7b'))
    address = '0x1E3c334E24ECD257Fd581Dc6F24489b13cff747b'
    privateKey = '0x03b4d5eef47eb20a7bb9cb1e61150137d5c91eaa5595c30c9a29fee9c0d29da0'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
