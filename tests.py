import unittest

from simproc import Simproc


class SMPTests(unittest.TestCase):

    def setUp(self):
        self.mp = Simproc()

    def test_nop(self):
        self.mp.execute('NOP')
        self.assertEqual(sum(self.mp.memory), 0)

    def test_mov_mem_val(self):
        self.mp.execute('MOV', '0', '10')
        self.assertEqual(self.mp.memory[0], 10)

    def test_mov_mem_mem_ref(self):
        self.mp.execute('MOV', '0', '10')
        self.mp.execute('MOV', '1', '[0]')
        self.assertEqual(self.mp.memory[1], 10)

    def test_mov_reg_val(self):
        self.mp.execute('MOV', 'r0', '10')
        self.assertEqual(self.mp.r0, 10)

    def test_mov_ref_mem_ref(self):
        self.mp.execute('MOV', '0', '10')
        self.mp.execute('MOV', 'r0', '[0]')
        self.assertEqual(self.mp.r0, 10)

    def test_inc_mem(self):
        self.mp.execute('INC', '0')
        self.assertEqual(self.mp.memory[0], 1)

    def test_dec_mem(self):
        self.mp.execute('MOV', '0', '2')
        self.mp.execute('DEC', '0')
        self.assertEqual(self.mp.memory[0], 1)

    def test_inc_reg(self):
        self.mp.execute('INC', 'r0')
        self.assertEqual(self.mp.r0, 1)

    def test_dec_reg(self):
        self.mp.execute('MOV', 'r0', '2')
        self.mp.execute('DEC', 'r0')
        self.assertEqual(self.mp.r0, 1)

    def test_jnz(self):
        self.mp.execute('MOV', 'r0', '1')
        self.mp.execute('JNZ', '10')
        self.assertEqual(self.mp.ip, 10)

    def test_jz(self):
        self.mp.execute('MOV', 'r0', '0')
        self.mp.execute('JZ', '10')
        self.assertEqual(self.mp.ip, 10)

    def test_jmp(self):
        self.mp.execute('JMP', '10')
        self.assertEqual(self.mp.ip, 10)
