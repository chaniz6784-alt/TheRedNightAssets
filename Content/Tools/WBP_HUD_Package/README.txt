
WBP_HUD_Package — Instructions (quick & simple)
==============================================

What this package does:
- Provides a Python script that, when run inside Unreal Editor's Python environment,
  creates 4 Widget Blueprints in your project under /Game/UI:
    * WBP_HUD
    * WBP_HealthBar
    * WBP_ManaBar
    * WBP_LootToast

Why this approach:
- Because raw .uasset files can be engine/version specific, this script uses Unreal's
  Editor Python API to create the widgets inside your project so they're compatible
  with your engine setup.

Steps — minimal (recommended)
1) Download and extract this ZIP into your project's Content folder. Example path:
   C:\Users\chani\Documents\Unreal Projects\TheRedNight\Content\Tools\WBP_HUD_Package

2) Open your project in Unreal Editor (make sure the Editor's Python plugin is enabled).
   - Edit -> Plugins -> search "Python" -> enable "Editor Scripting Utilities" and "Python Editor Script Plugin" if not already enabled.
   - Restart the Editor if you enabled them.

3) In the Editor go to: Window -> Developer Tools -> Output Log (or Python Console).
   In the Python Console run the script by executing:
   exec(open(r"{full_script_path}").read())

   Replace {full_script_path} with the actual path to the extracted file,
   e.g. r"C:\\Users\\chani\\Documents\\Unreal Projects\\TheRedNight\\Content\\Tools\\WBP_HUD_Package\\create_widgets.py"

4) After the script runs you will find the widgets in the Content Browser under /Game/UI.
   Right-click -> Fix Up Redirectors if needed.

5) To display the HUD at runtime:
   - Open your Player Controller or GameMode blueprint.
   - On BeginPlay: call "Create Widget" -> select WBP_HUD -> "Add to Viewport".
   - Optionally store the widget reference on the controller for later updates.

Additional notes:
- The created widgets are basic UMG layouts (size boxes, progress bars, simple text).
  You can open each widget and style them as you like (colors, fonts, anchors).
- If your Editor has strict path restrictions, run the script from the Editor's Python console.
- If any asset creation fails, check the Output Log for errors and share the error text with me.

That's it — I made it so you can run one command in Unreal and have the HUD files created.
If you want, after you run it I can give you a small Blueprint snippet to auto-set the GameMode / PlayerController wiring.
