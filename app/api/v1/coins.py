from flask import request, jsonify
from flask_login import login_required, current_user
from app.core.services.coins_service import CoinsService

def register(api):
    @api.route("/coins/balance")
    @login_required
    def balance():
        return jsonify({"balance": current_user.coins_balance})

    @api.route("/coins/add", methods=["POST"])
    @login_required
    def add():
        amount = request.json.get("amount")
        CoinsService.add_coins(current_user, amount, "Admin add")
        return jsonify({"status": "ok"})
