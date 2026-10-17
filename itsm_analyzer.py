import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Config gaya visualisasi
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

def generate_sample_servicenow_data(n=200):
    """
    Membuat dataset buatan (dummy) log incident ServiceNow
    apabila Anda belum menyediakan file CSV asli.
    """
    np.random.seed(42)
    categories = ['Software', 'Hardware', 'Network', 'Access/Identity', 'Database']
    
    created_dates = pd.date_range(start='2026-01-01', periods=n, freq='4h')
    
    data = {
        'number': [f'INC{10000 + i}' for i in range(n)],
        'category': np.random.choice(categories, n),
        'sys_created_on': created_dates,
        # Acknowledged time: created + random 5 to 120 minutes
        'sys_acknowledged_on': [dt + pd.Timedelta(minutes=int(np.random.exponential(25))) for dt in created_dates],
        # Resolved time: created + random 1 to 48 hours
        'resolved_at': [dt + pd.Timedelta(hours=int(np.random.exponential(12) + 1)) for dt in created_dates],
        # Technical Audit Score (0-100%)
        'technical_audit_score': np.random.uniform(70, 100, n),
        # User Satisfaction/Perception Score (1-5 scale)
        'user_satisfaction': np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.05, 0.1, 0.15, 0.4, 0.3])
    }
    return pd.DataFrame(data)

def analyze_itsm_incidents(df):
    """
    Mengolah data log incident untuk menghitung MTTA, MTTR, dan Audit Gap.
    """
    # 1. Pastikan kolom datetime terkonversi dengan benar
    df['sys_created_on'] = pd.to_datetime(df['sys_created_on'])
    df['sys_acknowledged_on'] = pd.to_datetime(df['sys_acknowledged_on'])
    df['resolved_at'] = pd.to_datetime(df['resolved_at'])

    # 2. Hitung MTTA & MTTR dalam satuan Jam (Hours)
    df['mtta_hours'] = (df['sys_acknowledged_on'] - df['sys_created_on']).dt.total_seconds() / 3600.0
    df['mttr_hours'] = (df['resolved_at'] - df['sys_created_on']).dt.total_seconds() / 3600.0

    # 3. Normalisasi User Perception Score ke skala 0-100% agar sejajar dengan Audit Score
    df['user_perception_pct'] = (df['user_satisfaction'] / 5.0) * 100.0

    # 4. Hitung Gap (Audit Teknis vs Persepsi User)
    df['audit_user_gap'] = df['technical_audit_score'] - df['user_perception_pct']

    return df

def generate_visualizations(df):
    """
    Menghasilkan ringkasan grafik analisis ITSM.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('ServiceNow Incident Operations & Gap Analysis Dashboard', fontsize=16, fontweight='bold')

    # Chart 1: Rata-Rata MTTR berdasarkan Kategori
    category_metrics = df.groupby('category')['mttr_hours'].mean().reset_index()
    sns.barplot(data=category_metrics, x='category', y='mttr_hours', ax=axes[0, 0], palette='Blues_d')
    axes[0, 0].set_title('Mean Time to Resolve (MTTR) by Category (Hours)', fontweight='bold')
    axes[0, 0].set_xlabel('Category')
    axes[0, 0].set_ylabel('Avg MTTR (Hours)')

    # Chart 2: Rata-Rata MTTA berdasarkan Kategori
    category_mtta = df.groupby('category')['mtta_hours'].mean().reset_index()
    sns.barplot(data=category_mtta, x='category', y='mtta_hours', ax=axes[0, 1], palette='Greens_d')
    axes[0, 1].set_title('Mean Time to Acknowledge (MTTA) by Category (Hours)', fontweight='bold')
    axes[0, 1].set_xlabel('Category')
    axes[0, 1].set_ylabel('Avg MTTA (Hours)')

    # Chart 3: Scatter Plot - Technical Audit Score vs User Perception
    sns.scatterplot(
        data=df, 
        x='technical_audit_score', 
        y='user_perception_pct', 
        hue='category', 
        alpha=0.7, 
        s=70, 
        ax=axes[1, 0]
    )
    # Garis Ideal (Tanpa Gap)
    axes[1, 0].plot([70, 100], [70, 100], color='red', linestyle='--', label='Ideal Alignment (No Gap)')
    axes[1, 0].set_title('User Perception (%) vs Technical Audit Score (%)', fontweight='bold')
    axes[1, 0].set_xlabel('Technical Audit Compliance Score (%)')
    axes[1, 0].set_ylabel('User Perception Score (%)')
    axes[1, 0].legend()

    # Chart 4: Distribusi Gap (Audit - User Perception)
    sns.histplot(df['audit_user_gap'], kde=True, ax=axes[1, 1], color='purple', bins=15)
    axes[1, 1].axvline(0, color='red', linestyle='--', label='Zero Gap')
    axes[1, 1].set_title('Distribution of Perception Gap (Audit % - User %)', fontweight='bold')
    axes[1, 1].set_xlabel('Gap Percentage Points')
    axes[1, 1].set_ylabel('Incident Count')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('itsm_analysis_dashboard.png', dpi=300)
    print("\n[INFO] Grafik dashboard berhasil disimpan sebagai 'itsm_analysis_dashboard.png'")
    plt.show()

# --- RUN EXECUTION ---
if __name__ == "__main__":
    # Jika Anda memiliki file CSV ServiceNow asli, muat seperti ini:
    # df_raw = pd.read_csv('servicenow_incidents.csv')
    
    print("[INFO] Menggenerasi data sampel ServiceNow...")
    df_raw = generate_sample_servicenow_data(n=250)

    print("[INFO] Memproses kalkulasi MTTR, MTTA, dan Gap Analysis...")
    df_processed = analyze_itsm_incidents(df_raw)

    # Menampilkan Ringkasan Eksekutif di Terminal
    print("\n" + "="*50)
    print("         RINGKASAN METRIK OPERASIONAL ITSM         ")
    print("="*50)
    print(f"Total Incident Diolah      : {len(df_processed)}")
    print(f"Rata-rata MTTA (Acknowledge): {df_processed['mtta_hours'].mean():.2f} jam")
    print(f"Rata-rata MTTR (Resolve)    : {df_processed['mttr_hours'].mean():.2f} jam")
    print(f"Rata-rata Audit Compliance  : {df_processed['technical_audit_score'].mean():.2f}%")
    print(f"Rata-rata User Perception   : {df_processed['user_perception_pct'].mean():.2f}%")
    print(f"Persepsi Gap Rata-rata      : {df_processed['audit_user_gap'].mean():.2f}% point")
    print("="*50)

    # Generasi Visualisasi
    generate_visualizations(df_processed)