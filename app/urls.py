from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academia/', include('specialty.urls')),
    path('academia/', include('instructor.urls')),
    path('academia/', include('students.urls')),
    path('academia/', include('plan.urls')),
    path('academia/', include('enrollment.urls')),
    path('academia/', include('exercise.urls')),
    path('academia/', include('workout.urls')),
    path('academia/', include('workoutexercise.urls')),
    path('academia/', include('assessment.urls')),
    path('academia/', include('payment.urls')),
    path('academia/', include('attendance.urls')),
]
