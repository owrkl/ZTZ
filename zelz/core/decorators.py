import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from ..Config import Config
from ..sql_helper.globals import gvarstatus

def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        # Explicit check for None instead of truthiness
        if c_q.query.user_id is not None and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in Config.SUDO_USERS
        ):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)  # Handling flood wait error
            except MessageNotModifiedError:
                pass  # If the message was not modified, we just pass
        else:
            # Fetch the custom help text, or fallback to default
            HELP_TEXT = (
                gvarstatus("HELP_TEXT")
                or "- عـذراً .. هـذه اللوحـه خاصـه بـ مـالك البـوت\n\n- قم بتنصيب بوت خاص بك من القناة @ZThon"
            )
            await c_q.answer(
                HELP_TEXT,
                alert=True,
            )

    return wrapper
