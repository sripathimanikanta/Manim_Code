from manim import *

class Updater(Scene):
	def construct(self):
		rotation_center = LEFT

		theta_tracker = ValueTracker(110)
		line1 = Line(LEFT, RIGHT)
		line_moving = Line(LEFT, RIGHT)
		line_ref = line_moving.copy()

		#exp -1 :
		# Not rotating but Projection
		# self.add(line1)
		# self.play(line_moving.animate.rotate(
		# 	theta_tracker.get_value() * DEGREES, about_point=rotation_center
		# ))

		line_moving.rotate(
			theta_tracker.get_value() * DEGREES, about_point=rotation_center
		)
		a = Angle(line1, line_moving, radius=0.5, other_angle=False)
		# tex = MathTex(r"\theta").move_to(
		# 	Angle(
		# 		line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
		# 	).point_from_proportion(0.5)
		# 	# point_from_proportion is in VMobject inherited from Mobject
		# )
		# exp 2:
		tex = Integer(theta_tracker.get_value()).scale(0.5).move_to(
				Angle(
					line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
				).point_from_proportion(0.5)
			)
		text1 = MathTex(f'^\circ').next_to(tex,RIGHT*(1/6)+UP*(1/6)).scale(0.5)
		# deg = str(angle.get_value())
		# tex = MathTex(f'{str(Integer(theta_tracker.get_value()).get_value())}^\circ').scale(0.5).move_to(
		# 	Angle(
		# 		line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
		# 	).point_from_proportion(0.5)
		# 	# point_from_proportion is in VMobject inherited from Mobject
		# )

		self.add(line1, line_moving, a, tex,text1)
		self.wait()

		line_moving.add_updater(
			lambda x: x.become(line_ref.copy()).rotate(
				theta_tracker.get_value() * DEGREES, about_point=rotation_center
			)
		)

		a.add_updater(
			lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
		)

		# tex.add_updater(
		# 	lambda x: x.become(
		# 		MathTex(f'{str(Integer(theta_tracker.get_value()).get_value())}^\circ').scale(0.5).move_to(
		# 			Angle(
		# 					line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
		# 			).point_from_proportion(0.5)
		# 		)
		# 	)
		# )
		tex.add_updater(
			lambda x: x.set_value(theta_tracker.get_value()).move_to(
				Angle(
					line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
				).point_from_proportion(0.5)
			)
		)

		text1.add_updater(
			lambda x: x.next_to(tex,RIGHT*(1/6)+UP*(1/6))
			)


		# exp:3
		# self.play(line1, line_moving, a, tex)
		# self.play(theta_tracker.animate.set_value(40))

		# tex.add_updater(
		# 	lambda x: x.move_to(
		# 		Angle(
		# 			line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
		# 		).point_from_proportion(0.5)
		# 	)
		# )

		self.play(theta_tracker.animate.set_value(40))
		self.play(theta_tracker.animate.increment_value(140))
		# self.play(tex.animate.set_color(RED), run_time=0.5)
		self.play(theta_tracker.animate.set_value(350))