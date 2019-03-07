import bitcoin.rpc

localrpc = bitcoin.rpc.Proxy()

# block
block = localrpc.getblock(localrpc.getblockhash(1)) # block num
print bitcoin.core.b2lx(block.GetHash()) # blockhash


print bitcoin.core.b2lx(block.calc_merkle_root()) # merkle tree root

# block header
print block.get_header() # block header
print block.get_header().difficulty # mining difficulty
print bitcoin.core.b2lx(block.get_header().hashMerkleRoot) # merkle tree root
print bitcoin.core.b2lx(block.get_header().hashPrevBlock) # prev blockhash
print block.get_header().nBits # blocksize
print block.get_header().nNonce # nonce
print block.get_header().nTime # timestamp
print block.get_header().nVersion # protocol version

# transaction
print len(block.vtx) # number of transactions
print block.vtx[0] # the first transaction