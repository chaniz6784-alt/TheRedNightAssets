
# install_all.py — TheRedNight: create basic HUD widgets and folders
# This runs inside Unreal Editor (UE5.5/5.6 compatible).
# It creates:
#   /Game/UI: WBP_HUD, WBP_HealthBar, WBP_ManaBar, WBP_LootToast
#   /Game/Blueprints placeholders (empty for now, ready to extend)
#   Optionally writes DefaultGame.ini hints for your project GameMode (commented)
#
import unreal

LOG_PREFIX = "TheRedNight Installer:"

def log(msg): unreal.log(f"{LOG_PREFIX} {msg}")
def warn(msg): unreal.log_warning(f"{LOG_PREFIX} {msg}")
def err(msg): unreal.log_error(f"{LOG_PREFIX} {msg}")

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
editor_asset = unreal.EditorAssetLibrary()
editor_util = unreal.EditorUtilityLibrary()

UI_PATH = "/Game/UI"
BP_PATH = "/Game/Blueprints"

def ensure_folder(path):
    if not editor_asset.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)
        log(f"Created folder: {path}")
    else:
        log(f"Folder exists: {path}")

def create_widget(name):
    factory = unreal.WidgetBlueprintFactory()
    try:
        asset = asset_tools.create_asset(name, UI_PATH, unreal.WidgetBlueprint, factory)
        editor_asset.save_asset(f"{UI_PATH}/{name}")
        log(f"Created widget: {UI_PATH}/{name}")
        return asset
    except Exception as e:
        err(f"Failed to create widget {name}: {e}")
        return None

def main():
    log("Starting...")

    ensure_folder(UI_PATH)
    ensure_folder(BP_PATH)

    widgets = ["WBP_HUD", "WBP_HealthBar", "WBP_ManaBar", "WBP_LootToast"]
    for w in widgets:
        if not editor_asset.does_asset_exist(f"{UI_PATH}/{w}"):
            create_widget(w)
        else:
            log(f"Widget already exists: {UI_PATH}/{w}")

    # Save all
    unreal.EditorAssetLibrary.save_directory(UI_PATH, only_if_is_dirty=False, recursive=True)
    log("Widgets created/saved. You can now open WBP_HUD and add Health/Mana bars & Loot Toast area.")

    # Tip: AutoHUD
    log("TIP: To show HUD without GameMode changes, add an Actor to the level that calls CreateWidget(WBP_HUD)->AddToViewport on BeginPlay.")
    log("Open your PlayerController or Level Blueprint and add the CreateWidget/AddToViewport nodes (quickest path).")

    # Redirectors
    unreal.EditorAssetLibrary.fixup_redirectors(UI_PATH)

    log("DONE")

if __name__ == "__main__":
    main()
