from collections import defaultdict
import heapq
import struct

class TreeNode:
    def __init__(self, symbol=None, frequency=None, left_child=None, right_child=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data: bytes):
    frequency_table = defaultdict(int)
    for byte in data:
        frequency_table[byte] += 1

    priority_queue = []
    for byte, freq in frequency_table.items():
        node = TreeNode(symbol=byte, frequency=freq)
        heapq.heappush(priority_queue, node)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        merged_node = TreeNode(frequency=left_node.frequency + right_node.frequency, left_child=left_node, right_child=right_node)
        heapq.heappush(priority_queue, merged_node)

    return heapq.heappop(priority_queue)

def generate_huffman_codes(node, current_code="", code_table=None):
    if code_table is None:
        code_table = {}

    if node is not None:
        if node.symbol is not None:
            code_table[node.symbol] = current_code
        generate_huffman_codes(node.left_child, current_code + "0", code_table)
        generate_huffman_codes(node.right_child, current_code + "1", code_table)

    return code_table

def serialize_tree(node):
    if node is None:
        return b""

    if node.symbol is not None:
        return b"\x01" + bytes([node.symbol])

    return b"\x00" + serialize_tree(node.left_child) + serialize_tree(node.right_child)

def deserialize_tree(data):
    def deserialize_helper():
        nonlocal index
        if index >= len(data):
            return None

        flag = data[index]
        index += 1

        if flag == 1:
            symbol = data[index]
            index += 1
            return TreeNode(symbol=symbol)
        elif flag == 0:
            left_child = deserialize_helper()
            right_child = deserialize_helper()
            return TreeNode(left_child=left_child, right_child=right_child)

    index = 0
    return deserialize_helper()

def ha_compress(input_data: bytes) -> bytes:
    if not input_data:
        return b""
    tree_root = build_huffman_tree(input_data)

    code_table = generate_huffman_codes(tree_root)

    encoded_bits = "".join([code_table[byte] for byte in input_data])

    padding_amount = 8 - len(encoded_bits) % 8
    encoded_bits += "0" * padding_amount
    encoded_bytes = bytearray()
    for i in range(0, len(encoded_bits), 8):
        byte = encoded_bits[i:i+8]
        encoded_bytes.append(int(byte, 2))

    tree_bytes = serialize_tree(tree_root)

    compressed_data = (bytes([padding_amount]) + struct.pack(">I", len(tree_bytes)) + tree_bytes + encoded_bytes)

    return compressed_data

def ha_decompress(compressed_data: bytes) -> bytes:
    if not compressed_data:
        return b""

    padding_amount = compressed_data[0]
    tree_size = struct.unpack(">I", compressed_data[1:5])[0]

    tree_bytes = compressed_data[5:5 + tree_size]
    tree_root = deserialize_tree(tree_bytes)

    encoded_bytes = compressed_data[5 + tree_size:]

    encoded_bits = "".join(f"{byte:08b}" for byte in encoded_bytes)
    encoded_bits = encoded_bits[:-padding_amount]

    decompressed_data = bytearray()
    current_node = tree_root
    for bit in encoded_bits:
        if bit == "0":
            current_node = current_node.left_child
        else:
            current_node = current_node.right_child

        if current_node.symbol is not None:
            decompressed_data.append(current_node.symbol)
            current_node = tree_root

    return bytes(decompressed_data)
