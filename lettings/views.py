# 🌐 Imports
import logging
from .models import Letting
from django.shortcuts import render


logger = logging.getLogger(__name__)


# 📄 Lettings Index View
def lettings_index(request):
    """Display a list of all lettings."""

    # 📋 Get all lettings
    lettings_list = Letting.objects.all()

    # 🧩 Context for the template
    context = {'lettings_list': lettings_list}

    # 🖼️ Render lettings index template
    return render(request, 'lettings/index.html', context)


# 🔍 Letting Detail View
def get_letting(request, letting_id):
    """Display the details of a specific letting by ID."""
    try:
        # 🎯 Critical point: DB lookup
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting_details.html', context)
    except Exception:
        # 🚨 Log error with traceback + context
        logger.exception("Failed to render letting detail",
                         extra={"letting_id": letting_id,
                                "path": request.path,
                                "method": request.method})
        # 🔁 Re-raise → Django returns a 500, Sentry captures it automatically
        raise
