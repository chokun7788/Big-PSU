from pathlib import Path

path = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tests\test_p0_calendar_booking_reconciliation_20260925.py")
text = path.read_text(encoding="utf-8")
old = '''    def test_dashboard_date_override_cannot_open_lunch(self) -> None:
'''
new = '''    def test_vr_half_hour_reservation_blocks_the_full_hour(self) -> None:
        schedule = dashboard.default_center_schedule()
        with patch.object(dashboard, "load_center_schedule", return_value=schedule), patch.object(
            dashboard, "now_bangkok", return_value=datetime(2026, 9, 29, 8, 0)
        ):
            status = dashboard.build_status(
                dashboard.parse_csv(
                    "id,service_id,day,time,duration,status\\n"
                    "1,8,2026-09-29,09:00,30,approved\\n"
                ),
                dashboard.parse_csv("id,name,duration\\n8,VR Station (Morning),30\\n"),
                "2026-09-29",
                {"mode": "remote_csv_live", "appointments_meta": {"hash": "fixture"}, "services_meta": {"hash": "fixture"}},
            )
        slot = next(s for s in status["services"][0]["slots"] if s["start"] == "09:00")
        self.assertEqual((slot["end"], slot["status"], slot["available_count"]), ("10:00", "busy", 0))
        live = _snapshot_from_payload(dashboard.chatbot_status_payload(status))
        self.assertIn("0/1", render_live_booking_answer("Is VR free from 09:30 to 10:00?", live, "en"))

    def test_dashboard_date_override_cannot_open_lunch(self) -> None:
'''
if text.count(old) != 1:
    raise RuntimeError(f"Expected one insertion point; got {text.count(old)}")
path.write_text(text.replace(old, new), encoding="utf-8")
print("Added owner-confirmed VR hourly blocking regression test.")
