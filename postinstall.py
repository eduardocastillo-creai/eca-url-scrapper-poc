import subprocess


def install_playwright():
    """Run playwright install to set up required browsers."""
    try:
        print("Installing Playwright browsers...")
        subprocess.run(["playwright", "install"], check=True)
        print("Playwright installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error during Playwright installation.")
        print(f"Details: {e}")
        raise


if __name__ == "__main__":
    install_playwright()
