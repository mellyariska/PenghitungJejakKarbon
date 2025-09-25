import streamlit as st

# Fungsi perhitungan emisi karbon
# Jejak Karbon Harian: Kalkulator Sederhana

def calculate_transport_emissions(distance_km, mode):
    """
    Menghitung emisi karbon dari transportasi.
    Args:
        distance_km (float): Jarak perjalanan dalam kilometer.
        mode (str): Mode transportasi ('mobil', 'motor', 'bus', 'sepeda', 'jalan_kaki').
    Returns:
        float: Emisi karbon dalam kg CO2.
    """
    emissions_factor = {
        'mobil': 0.21,       # kg CO2 per km
        'motor': 0.12,       # kg CO2 per km
        'bus': 0.05,         # kg CO2 per km
        'sepeda': 0.0,       # kg CO2 per km
        'jalan_kaki': 0.0    # kg CO2 per km
    }
    return distance_km * emissions_factor.get(mode, 0)

def calculate_energy_emissions(energy_kwh):
    """
    Menghitung emisi karbon dari konsumsi energi listrik.
    Args:
        energy_kwh (float): Konsumsi listrik dalam kWh.
    Returns:
        float: Emisi karbon dalam kg CO2.
    """
    emissions_factor = 0.85  # kg CO2 per kWh (angka rata-rata global, dapat disesuaikan)
    return energy_kwh * emissions_factor

def calculate_food_emissions(diet):
    """
    Menghitung emisi karbon berdasarkan pola makan.
    Args:
        diet (str): Jenis pola makan ('omnivora', 'vegetarian', 'vegan').
    Returns:
        float: Emisi karbon dalam kg CO2 per hari.
    """
    emissions_factor = {
        'omnivora': 7.0,    # kg CO2 per hari
        'vegetarian': 4.0,  # kg CO2 per hari
        'vegan': 2.5        # kg CO2 per hari
    }
    return emissions_factor.get(diet, 0)

def main():
    print("=== Kalkulator Jejak Karbon Harian ===")

    # Input transportasi
    distance_km = float(input("Masukkan jarak perjalanan (km): "))
    mode = input("Masukkan mode transportasi (mobil, motor, bus, sepeda, jalan_kaki): ").lower()
    transport_emissions = calculate_transport_emissions(distance_km, mode)

    # Input konsumsi energi
    energy_kwh = float(input("Masukkan konsumsi listrik harian (kWh): "))
    energy_emissions = calculate_energy_emissions(energy_kwh)

    # Input pola makan
    diet = input("Masukkan pola makan (omnivora, vegetarian, vegan): ").lower()
    food_emissions = calculate_food_emissions(diet)

    # Total emisi karbon
    total_emissions = transport_emissions + energy_emissions + food_emissions

    # Output hasil
    print("\n=== Hasil Jejak Karbon ===")
    print(f"Emisi dari transportasi: {transport_emissions:.2f} kg CO2")
    print(f"Emisi dari konsumsi energi: {energy_emissions:.2f} kg CO2")
    print(f"Emisi dari pola makan: {food_emissions:.2f} kg CO2")
    print(f"Total emisi harian: {total_emissions:.2f} kg CO2")

if __name__ == "__main__":
    main()

