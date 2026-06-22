import unittest
from energy_monitor import calculate_energy_financials

class TestEnergyFinancials(unittest.TestCase):

    def test_under_discount_threshold(self):
        """1. Ca kiểm thử dưới ngưỡng chiết khấu (< 50,000 kWh) -> Chiết khấu 0%"""
        devices = [
            {'id': 'T01', 'location': 'Shop A', 'old_index': 0, 'new_index': 20000, 'status': 'Normal'},
            {'id': 'T02', 'location': 'Shop B', 'old_index': 0, 'new_index': 25000, 'status': 'Normal'}
        ] # Tổng tiêu thụ = 45,000 kWh
        
        total_kwh, discount, total_money = calculate_energy_financials(devices)
        
        self.assertEqual(total_kwh, 45000)
        self.assertEqual(discount, 0)
        self.assertEqual(total_money, 45000 * 3000) # Đạt 135,000,000 VND

    def test_at_discount_threshold(self):
        """2. Ca kiểm thử chạm chính xác mốc biên chiết khấu (= 50,000 kWh) -> Chiết khấu 3%"""
        devices = [
            {'id': 'T01', 'location': 'Shop A', 'old_index': 0, 'new_index': 50000, 'status': 'Normal'}
        ] # Tổng tiêu thụ = 50,000 kWh
        
        total_kwh, discount, total_money = calculate_energy_financials(devices)
        
        self.assertEqual(total_kwh, 50000)
        self.assertEqual(discount, 3)
        expected_money = int((50000 * 3000) * 0.97)
        self.assertEqual(total_money, expected_money) # Đạt 145,500,000 VND

    def test_over_discount_threshold(self):
        """3. Ca kiểm thử vượt mốc chiết khấu (Ví dụ: 60,000 kWh giống ảnh mô tả SRS) -> Chiết khấu 3%"""
        devices = [
            {'id': 'T01', 'location': 'Shop A', 'old_index': 0, 'new_index': 40000, 'status': 'Normal'},
            {'id': 'T02', 'location': 'Shop B', 'old_index': 0, 'new_index': 20000, 'status': 'Normal'}
        ] # Tổng tiêu thụ = 60,000 kWh
        
        total_kwh, discount, total_money = calculate_energy_financials(devices)
        
        self.assertEqual(total_kwh, 60000)
        self.assertEqual(discount, 3)
        expected_money = int((60000 * 3000) * 0.97)
        self.assertEqual(total_money, expected_money) # Đạt 174,600,000 VND

if __name__ == '__main__':
    unittest.main()