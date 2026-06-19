import os
from PIL import Image
import glob

def fix_and_convert_ppm(ppm_path, png_path):
    # Try opening directly first
    try:
        with Image.open(ppm_path) as img:
            img.save(png_path, "PNG")
        return True
    except Exception as e:
        print(f"Direct conversion failed for '{ppm_path}' ({e}). Attempting to recover truncated PPM...")

    # If it failed, let's parse and pad the PPM data
    try:
        with open(ppm_path, 'r') as f:
            lines = f.readlines()
            
        if not lines or lines[0].strip() != 'P3':
            print(f"File '{ppm_path}' is not a valid P3 PPM file.")
            return False
            
        # Extract width, height, maxval
        header_lines = []
        pixel_lines = []
        for line in lines:
            line_strip = line.strip()
            if not line_strip or line_strip.startswith('#'):
                continue
            if len(header_lines) < 3:
                header_lines.append(line_strip)
            else:
                pixel_lines.append(line_strip)
                
        if len(header_lines) < 3:
            print(f"Could not parse header of '{ppm_path}'.")
            return False
            
        width, height = map(int, header_lines[1].split())
        maxval = int(header_lines[2])
        total_pixels_needed = width * height
        
        # Parse existing pixels (some lines might contain multiple pixels or parts of pixels)
        pixels = []
        for pl in pixel_lines:
            parts = pl.split()
            # Group into chunks of 3 if they are on the same line, or append values
            pixels.extend(parts)
            
        # We need 3 values per pixel
        total_vals_needed = total_pixels_needed * 3
        current_vals = len(pixels)
        
        if current_vals < total_vals_needed:
            missing_vals = total_vals_needed - current_vals
            print(f"PPM is truncated. Read {current_vals // 3} of {total_pixels_needed} pixels. Padding with {missing_vals // 3} black pixels...")
            pixels.extend(['0'] * missing_vals)
        else:
            pixels = pixels[:total_vals_needed]
            
        # Write a temporary fixed PPM
        temp_ppm_path = ppm_path + ".temp_fixed.ppm"
        with open(temp_ppm_path, 'w') as f:
            f.write("P3\n")
            f.write(f"{width} {height}\n")
            f.write(f"{maxval}\n")
            # Write pixels grouped by 3 (one pixel per line for simplicity)
            for idx in range(0, len(pixels), 3):
                f.write(" ".join(pixels[idx:idx+3]) + "\n")
                
        # Now convert the fixed PPM
        with Image.open(temp_ppm_path) as img:
            img.save(png_path, "PNG")
            
        # Clean up temp file
        os.remove(temp_ppm_path)
        print(f"Successfully recovered and converted '{ppm_path}' to '{png_path}'.")
        return True
    except Exception as recovery_error:
        print(f"Failed to recover '{ppm_path}': {recovery_error}")
        if os.path.exists(temp_ppm_path):
            os.remove(temp_ppm_path)
        return False

def convert_all():
    ppm_dir = os.path.join("renders", "ppm")
    png_dir = os.path.join("renders", "png")
    
    if not os.path.exists(ppm_dir):
        print(f"Directory '{ppm_dir}' not found.")
        return
        
    os.makedirs(png_dir, exist_ok=True)

    ppm_files = glob.glob(os.path.join(ppm_dir, "*.ppm"))
    if not ppm_files:
        print("No .ppm files found in the 'renders/ppm' directory.")
        return

    print(f"Found {len(ppm_files)} PPM files. Starting conversion...")
    
    success_count = 0
    for ppm_path in ppm_files:
        filename = os.path.basename(ppm_path)
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(png_dir, png_filename)
        
        # Check if PNG already exists and is newer than PPM
        if os.path.exists(png_path) and os.path.getmtime(png_path) > os.path.getmtime(ppm_path):
            print(f"Skipping '{ppm_path}' (PNG is up to date).")
            success_count += 1
            continue
            
        if fix_and_convert_ppm(ppm_path, png_path):
            success_count += 1
            
    print(f"\nFinished! Converted/Verified {success_count} of {len(ppm_files)} files.")

if __name__ == "__main__":
    convert_all()
