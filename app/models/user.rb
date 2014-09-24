class User < ActiveRecord::Base
	validates :username, presence: true, uniqueness: true, length: { maximum:128}
	validates_length_of :password, :maximum => 128
end
